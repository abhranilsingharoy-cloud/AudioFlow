import os
import io
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_get(client):
    rv = client.get('/')
    assert rv.status_code == 200
    assert b'AudioFlow' in rv.data or b'Upload' in rv.data or b'<!DOCTYPE html>' in rv.data

def test_index_post_no_file(client):
    rv = client.post('/')
    assert rv.status_code == 200
    assert b'No file uploaded' in rv.data or b'No file selected' in rv.data
