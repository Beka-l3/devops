# this is an official Python runtime, used as the parent image
FROM python:3.9-slim

# set the working directory in the container to /app
WORKDIR /app

COPY pyproject.toml .
COPY pdm.lock .

# execute everyone's favorite pip command, pip install -r
RUN pip install --no-cache-dir pdm==1.8.0 &&\
    pdm install

# unblock port 80 for the Flask app to run on
EXPOSE 80

COPY . .

# execute the Flask app
CMD pdm run python app.py

