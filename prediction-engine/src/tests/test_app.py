import pytest
from flask.testing import FlaskClient
from app import app


@pytest.fixture
def client() -> FlaskClient:
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_predict(client: FlaskClient) -> None:
    response = client.post("/predict", json={
        "temperature": 25.0,
        "humidity": 50.0,
        "wind_speed": 3.0
    })
    assert response.status_code == 200
    assert "predictions" in response.get_json()
