import requests
import os

from langchain_core.language_models import LLM, SimpleChatModel
from langchain_core.callbacks import CallbackManagerForLLMRun
from langchain_core.messages import BaseMessage
from typing import Optional, Any, List

import jinja2


class Zephyr(LLM):

    endpoint: str = "https://progai.prognostica.de/zephyr-7b-beta"
    stop: List[str] = ["<s>", "</s>", "<|user|>"]
    temperature: float = 0.8
    top_k: int = 40
    top_p: float = 1.0

    def _llm_type():
        return "zephyr-7b-beta"

    def _call(
        self,
        prompt: str,
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        res = requests.post(
            self.endpoint,
            json={
                "prompt": prompt,
                "stream": False,
                "stop": stop if stop is not None else self.stop,
                "temperature": self.temperature,
                "top_k": self.top_k,
                "top_p": self.top_p,
            },
            headers={"Authorization": f"Bearer {os.getenv('PROGAI_TOKEN')}"},
        )
        if res.status_code != 200:
            raise requests.HTTPError()
        data = res.json()
        if data["truncated"] == True:
            raise RuntimeWarning("Exeeded context length.")
        return data.get("content")


class ZephyrChat(SimpleChatModel, Zephyr):
    def _llm_type():
        return "zephyr-7b-beta-chat"

    _jinja2_template: str = (
        "{% for m in messages %}"
        "{% if m.type=='system' %}<|system|>"
        "{% elif m.type=='human' %}<|user|>"
        "{% else %}<|assistant|>{% endif %}"
        "\n{{ m.content }}</s> \n{% endfor %}"
        "<|assistant|>\n{{ start }}"
    )
    ai_message_start: str = ""

    def _call(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[CallbackManagerForLLMRun] = None,
        **kwargs: Any,
    ) -> str:
        start = kwargs["ai_message_start"] if "ai_message_start" in kwargs else self.ai_message_start
        prompt = jinja2.Environment().from_string(
            self._jinja2_template).render(messages=messages, start=start)
        return Zephyr._call(self, prompt=prompt, stop=stop,
                            run_manager=run_manager, kwargs=kwargs)
