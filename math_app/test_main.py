from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_minimum():
    response = client.post(
    "/min/",
    json={"numbers":[20, 4, 30, -5], "quantifier":4},
    )
    assert response.status_code == 200
    assert response.json() == -5

def test_minimum_empty_list():
    response = client.post(
    "/min/",
    json={"numbers":[], "quantifier":4},
    )
    assert response.status_code == 422

def test_minimum_invalid_list():
    response = client.post(
    "/min/",
    json={"numbers":["a"], "quantifier":4},
    )
    assert response.status_code == 422

def test_minimum_missing_body():
    response = client.post(
    "/min/",
    )
    assert response.status_code == 422

def test_maximum():
    response = client.post(
    "/max/",
    json={"numbers":[20, 4, 30, -5], "quantifier":4},
    )
    assert response.status_code == 200
    assert response.json() == 30

def test_average():
    response = client.post(
    "/avg/",
    json={"numbers":[20, 50, 30, -50]},
    )
    assert response.status_code == 200
    assert response.json() == 12.5

def test_median():
    response = client.post(
    "/median/",
    json={"numbers":[20, 4, 30, 50]},
    )
    assert response.status_code == 200
    assert response.json() == 25

def test_percentile():
    response = client.post(
    "/percentile/",
    json={"numbers":[20, 4, 30, -5], "quantifier":25},
    )
    assert response.status_code == 200
    assert response.json() == -5


test_minimum()
test_minimum_empty_list()
test_minimum_invalid_list()
test_minimum_missing_body()
test_maximum()
test_average()
test_median()
test_percentile()

print("tests passed")
