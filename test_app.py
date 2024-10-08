import os
import io
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    
    # Asegúrate de que la carpeta 'uploads/' exista
    if not os.path.exists('./uploads'):
        os.makedirs('./uploads')
    
    yield client

def test_upload_form(client):
    response = client.get('/')
    assert response.status_code == 200

def test_upload_file(client):
    # Simula un archivo subido
    data = {'file': (io.BytesIO(b"some file data"), 'test.txt')}
    response = client.post('/upload', data=data, content_type='multipart/form-data')
    assert response.status_code == 200
    assert b'File successfully uploaded' in response.data