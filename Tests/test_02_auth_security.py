import pytest
import requests
from Utils.payloads import updated_booking_payload
import allure

@allure.feature("Security")
@allure.story("Authentication")
@allure.title("Auth with Invalid Credentials")
@pytest.mark.security
def test_auth_invalid_credentials(base_url):
    credentials = {"username": "admin", "password": "wrongpassword"}
    response = requests.post(f"{base_url}/auth", json = credentials)
    assert response.status_code == 200
    assert "token" not in response.json(), "Authentication should fail with invalid credentials"

@allure.feature("Security")
@allure.story("Authentication")
@allure.title("Auth with Missing Fields")
@pytest.mark.security
def test_auth_missing_fields(base_url):
    credentials = {"username": "admin"} 
    response = requests.post(f"{base_url}/auth", json = credentials)
    assert response.status_code == 200
    assert "token" not in response.json(), "Authentication should fail when password is missing"

@allure.feature("Security")
@allure.story("Authorization")
@allure.title("Update Booking without Token")
@pytest.mark.security
def test_update_booking_without_token(base_url, headers, booking_id):
    payload = updated_booking_payload()
    response = requests.put(f"{base_url}/booking/{booking_id}", json = payload, headers = headers)
    assert response.status_code == 403, "Should return 403 Forbidden when no token is provided"

badtoken = "badtoken"
@allure.feature("Security")
@allure.story("Authorization")
@allure.title("Update Booking with Malformed Token")
@pytest.mark.security
def test_update_booking_with_malformed_token(base_url, booking_id, headers):
    malformed_header = {"Cookie": f"token={badtoken}"} 
    final_headers = headers.copy()
    final_headers.update(malformed_header)
    payload = updated_booking_payload()
    response = requests.put(f"{base_url}/booking/{booking_id}", json = payload, headers = final_headers)
    assert response.status_code == 403, "Should return 403 Forbidden when using a malformed token"

@allure.feature("Security")
@allure.story("Authorization")
@allure.title("Delete Booking without Token")
@pytest.mark.security
def test_delete_booking_without_token(base_url, headers, booking_id):
    response = requests.delete(f"{base_url}/booking/{booking_id}", headers = headers)
    assert response.status_code == 403, "Should return 403 Forbidden when no token is provided"
