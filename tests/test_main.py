# tests/test_hello.py
from src.hello import say_hello

def test_say_hello():
    assert say_hello() == "Hello, World!"