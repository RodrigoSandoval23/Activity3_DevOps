# tests/test_app.py
import pytest
from app.app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_status_code(client):
    """Verifica que la ruta principal responda correctamente"""
    response = client.get('/')
    assert response.status_code == 200

def test_home_data(client):
    """Verifica que el mensaje sea el correcto"""
    response = client.get('/')
    data = response.get_json()
    assert data["message"] == "¡Hola desde Flask en Docker!"