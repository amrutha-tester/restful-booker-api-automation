import pytest
import requests

# Base URL fixture
@pytest.fixture(scope="session")
def base_url():
    return "https://restful-booker.herokuapp.com"

# Authentication token fixture
@pytest.fixture(scope="session")
def auth_token(base_url):
    payload = {
        "username": "admin",
        "password": "password123"
    }
    response = requests.post(f"{base_url}/auth", json=payload)
    # Error handling for authentication failure
    if response.status_code != 200:
        pytest.fail(f"Authentication failed with status code {response.status_code}: {response.text}")
    token = response.json().get("token")
    return token

# Common headers fixture
@pytest.fixture(scope="session")
def headers(auth_token):
    return {
        "Content-Type": "application/json",
        "Accept": "application/json",
    }

# Cookies fixture
@pytest.fixture
def auth_cookie(auth_token):
    return {"Cookie": f"token={auth_token}"}

# Booking ID fixture (example of a dynamic fixture that can be used in tests)
@pytest.fixture
def booking_payload():
    return {
        "firstname": "Ariana",
        "lastname": "James",
        "totalprice": 200,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2018-02-01"
        },
        "additionalneeds": "Breakfast"
    }