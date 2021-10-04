FROM python:3.9-slim
WORKDIR /app

RUN adduser --disabled-password beka && chown -R beka /app
RUN mkdir /pyapp-tmp-dir && chown -R beka /pyapp-tmp-dir

# USER beka

COPY pyproject.toml .
COPY pdm.lock .
RUN pip3 install --no-cache-dir pdm==1.8.0
RUN python -m pdm install

EXPOSE 80

COPY . .
CMD python -m pdm run python app.py
