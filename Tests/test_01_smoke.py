import pytest
import requests
from jsonschema import validate
from Utils.schemas import AUTH_SCHEMA, BOOKING_SCHEMA, CREATE_BOOKING_RESPONSE_SCHEMA
import allure

@allure.feature("Smoke Tests")
@allure.story("Service Health")
@allure.title("Verify API Ping")
@pytest.mark.smoke
def test_ping(base_url):
    response = requests.get(f"{base_url}/ping")
    assert response.status_code == 201, f"Expected status code 201, got {response.status_code}"
    assert response.text == "Created", f"Expected response text 'Created', got '{response.text}'"

@allure.feature("Smoke Tests")
@allure.story("Authentication")
@allure.title("Verify Auth Token Generation")
@pytest.mark.smoke
def test_create_token_smoke(auth_token):
    assert auth_token is not None, "Authentication token should not be None"
    validate(schema=AUTH_SCHEMA, instance={"token": auth_token})

@allure.feature("Smoke Tests")
@allure.story("Booking Management")
@allure.title("Verify Basic Booking Creation")
@pytest.mark.smoke
def test_create_booking_smoke(base_url, auth_token, booking_payload):
    response = requests.post(f"{base_url}/booking", json=booking_payload)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    response_data = response.json()
    validate(schema=CREATE_BOOKING_RESPONSE_SCHEMA, instance=response_data)
    