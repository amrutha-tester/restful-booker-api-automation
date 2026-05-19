import pytest
import requests
from jsonschema import validate
from Utils.schemas import AUTH_SCHEMA, CREATE_BOOKING_RESPONSE_SCHEMA
import allure

@allure.feature("Schema Validation")
@allure.story("Auth Schema")
@allure.title("Validate Authentication Response Schema")
@pytest.mark.schema
def test_create_token_schema(auth_token):
    assert auth_token is not None, "Auth token should not be None"
    validate(schema=AUTH_SCHEMA, instance={"token": auth_token})

@allure.feature("Schema Validation")
@allure.story("Booking Schema")
@allure.title("Validate Create Booking Response Schema")
@pytest.mark.schema
def test_create_booking_response_schema(base_url, auth_token, booking_payload):
    response = requests.post(f"{base_url}/booking", json=booking_payload)
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    response_data = response.json()
    validate(schema=CREATE_BOOKING_RESPONSE_SCHEMA, instance=response_data)