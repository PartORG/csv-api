"""
File with minimal set ou unittests for created API.
"""

from fastapi.testclient import TestClient

from main import app

# init TestClient based on created main API app
client = TestClient(app)


# Test 1
def test_get_all_info():
    """
    Test case to get all information data from information table.
    :return:
    """
    response = client.get("/info/")
    assert response.status_code == 200
    assert len(response.json()) == 5


# Test 2
def test_get_info_netterden():
    """
    Test case to get an information of a specific Park.
    :return:
    """
    response = client.get("/info/?park=Netterden")
    assert response.status_code == 200
    assert len(response.json()) == 1


# Test 3
def test_get_info_solar():
    """
    Test case to get all Park data that use Solar energy.
    :return:
    """
    response = client.get("/info/?energy_type=Solar")
    assert response.status_code == 200
    assert len(response.json()) == 2


# Test 4
def test_get_prod_bemmel_10():
    """
    TEst case to get production data from Bemmel park - for an empty period it returns 10 last data entries.
    :return:
    """
    response = client.get("/prod/period/?park_name=Bemmel")
    assert response.status_code == 200
    assert len(response.json()) == 10


# Test 5
def test_get_prod_bemmel_period():
    """
    Test case to get a produced power from Bemmel park for a chosen period.
    :return:
    """
    response = client.get("/prod/period/?park_name=Bemmel&start_date=2020-01-01%2001%3A01%3A00&"
                          "end_date=2020-01-01%2001%3A45%3A00")
    assert response.status_code == 200
    assert len(response.json()) == 3


# TODO: Here can be added more tests and more complex tests that would use fixtures and utility functions.

