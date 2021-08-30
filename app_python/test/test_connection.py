import pytest
import requests

def test_app():
    assert requests.get('http://127.0.0.1:5000/').status_code == 200

