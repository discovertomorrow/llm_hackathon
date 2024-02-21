FROM python:3.11

# Install packages.
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt

# Copy sample data.
COPY data /app
