from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():

    response = client.get("/")

    assert response.status_code == 200

    assert response.json() == {
        "message": "Smart Expense Tracker API Running"
    }


def test_add_expense():

    data = {
        "title": "Burger",
        "amount": 300,
        "category": "Food"
    }

    response = client.post("/expenses", json=data)

    assert response.status_code == 200

    assert response.json() == {
        "message": "Expense Added Successfully"
    }


def test_get_expenses():

    response = client.get("/expenses")

    assert response.status_code == 200

    assert isinstance(response.json(), list)