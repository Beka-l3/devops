# devops

This is python application on flask showing time in Europe/Moscow

## Installation
Command consequencies:
```
git clone https://github.com/Beka-l3/devops.git
cd app_python
pip install pdm
pdm install
```

## Run
Command consequencies:
```
pdm run python3 app.py
```

Application uses port 80
Browse: localhost:80

# Docker

Image is on my dockerhub

## Pull
```
docker pull beka13/python_app
```

## Run
```
docker run -p <local port>:80 beka13/python_app
```
