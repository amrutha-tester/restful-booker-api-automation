import pytest
import requests
from Utils.payloads import invalid_booking_payload_missing_firstname, invalid_booking_payload_bad_price, invalid_booking_payload_bad_dates
import allure

@allure.feature("Negative Testing")
@allure.story("Creation Failures")
@allure.title("Create Booking Missing Required Firstname")
@pytest.mark.negative
def test_create_booking_missing_firstname(base_url):
    payload = invalid_booking_payload_missing_firstname()
    response = requests.post(f"{base_url}/booking", json=payload)
    assert response.status_code == 400, f"Expected status code 400, got {response.status_code}"

@allure.feature("Negative Testing")
@allure.story("Creation Failures")
@allure.title("Create Booking with Invalid Price Data Type")
@pytest.mark.negative
def test_create_booking_bad_price(base_url):
    payload = invalid_booking_payload_bad_price()
    response = requests.post(f"{base_url}/booking", json = payload)
    assert response.status_code == 400, f"Expected status code 400, got {response.status_code}"

@allure.feature("Negative Testing")
@allure.story("Creation Failures")
@allure.title("Create Booking with Invalid Date Logic")
@pytest.mark.negative
def test_create_booking_bad_dates(base_url):
    payload = invalid_booking_payload_bad_dates()
    response = requests.post(f"{base_url}/booking", json = payload)
    assert response.status_code == 400, f"Expected status code 400, got {response.status_code}"