import pytest
import requests
import time

def test_delay():
    start = time.time()
    code = requests.get('http://127.0.0.1:5000/').status_code
    
    if code == 200:
        end = time.time()
    
    delay = end - start

    assert delay <= 1
