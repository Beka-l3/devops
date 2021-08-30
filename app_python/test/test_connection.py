import pytest
import requests
import time
from flask.testing import FlaskClient
from app import app

app.testing = True
client = app.test_client()

def test_app():
    start = time.time()

    assert client.get('http://127.0.0.1:5000/').status_code == 200

    end = time.time()
    delay = end - start

    assert delay <= 1

