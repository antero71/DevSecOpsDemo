# tests/test_app.py

from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello from DevSecOps Demo!" in response.data

def test_echo():
    client = app.test_client()
    response = client.get("/echo?input=testi")
    assert response.status_code == 200
    assert b"You sent: testi" in response.data