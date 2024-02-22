# Welcome to the llm_hackathon repo from prognostica
Start with the installation instructions in `install.ipynb`.\
Feel free to use the provided `Dockerfile`.\
The API token which is to be set in the created .env file will be given during the actual hackathon session.
Once the installation is finished, you can start interacting with the remote open source llm using `cutom_llm_interaction.ipynb`.

# The Task
The task will be to generate a text summary of a forecasting report providing highlights and general insights.\
The report (see `data/forecast_report.csv`) will be of the form : 


|    | business_unit   | product_family   |   forecast_previous_month_production_2024 |   forecast_current_month_production_2024 |   forecast_current_month_marketing_2024 |   possible_supply_for_2024 |
|---:|:---------------|:-----------------|------------------------------------------:|-----------------------------------------:|----------------------------------------:|---------------------------:|
|  0 | AL             | Prozil           |                                       103 |                                      104 |                                     120 |                        100 |
|  1 | AL             | Focix            |                                       789 |                                      631 |                                     770 |                       1000 |
|  2 | AL             | Zentra           |                                        42 |                                       34 |                                      35 |                         50 |
|  3 | AL             | Optix            |                                       957 |                                      766 |                                     800 |                        500 |
|  4 | AL             | Mentix           |                                       221 |                                      177 |                                     200 |                        500 |



## Happy Hacking :)

Feel free to fork and share your hacking results!