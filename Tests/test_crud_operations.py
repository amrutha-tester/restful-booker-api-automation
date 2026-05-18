import pytest
import requests
from jsonschema import validate
from Utils.schemas import CREATE_BOOKING_RESPONSE_SCHEMA
from Utils.payloads import updated_booking_payload
booking_id = None

@pytest.mark.crud
def test_create_booking(base_url,booking_payload):
    create_response = requests.post(f"{base_url}/booking", json=booking_payload)
    assert create_response.status_code == 200, f"Expected status code 200, got {create_response.status_code}"
    validate(schema=CREATE_BOOKING_RESPONSE_SCHEMA, instance=create_response.json())
    global booking_id
    booking_id = create_response.json().get("bookingid")


@pytest.mark.crud
def test_get_booking(base_url):
    get_booking_response = requests.get(f"{base_url}/booking/{booking_id}")
    assert get_booking_response.status_code == 200, f"Expected status code 200, got {get_booking_response.status_code}"
    assert get_booking_response.json().get("firstname") == "Ariana", "Firstname does not match expected value"

@pytest.mark.crud
def test_get_nonexistent_booking(base_url):
    non_existent_id = 999999
    response = requests.get(f"{base_url}/booking/{non_existent_id}")
    assert response.status_code == 404, f"Expected status code 404 for non-existent booking, got {response.status_code}"

@pytest.mark.crud
def test_update_booking(base_url, headers, auth_cookie):
    payload = updated_booking_payload()
    update_response = requests.patch(f"{base_url}/booking/{booking_id}", json=payload, headers = headers, cookies = auth_cookie)
    assert update_response.status_code == 200, f"Expected status code 200, got {update_response.status_code}"
    assert update_response.json().get("lastname") == "Grande", "Lastname was not updated correctly"

@pytest.mark.crud
def test_delete_booking(base_url, headers, auth_cookie):
    delete_response = requests.delete(f"{base_url}/booking/{booking_id}", headers = headers, cookies = auth_cookie)
    assert delete_response.status_code == 201, f"Expected status code 201, got {delete_response.status_code}"

@pytest.mark.crud
def test_confirm_booking_deletion(base_url):
    confirm_response = requests.get(f"{base_url}/booking/{booking_id}")
    assert confirm_response.status_code == 404, f"Expected status code 404 for deleted booking, got {confirm_response.status_code}"
