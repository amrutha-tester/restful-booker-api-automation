import pytest
import requests

@pytest.mark.integration

def test_booking_lifecycle(base_url,headers,booking_payload):
    credentials = {"username": "admin", "password": "password123"}
    # Get auth token
    auth_response = requests.post(f"{base_url}/auth", json=credentials)
    assert auth_response.status_code ==200, f"Authentication failed with status code {auth_response.status_code}: {auth_response.text}"
    token = auth_response.json().get("token")

    headers = {"Cookie": f"token={token}"}

    # Create booking
    create_response = requests.post(f"{base_url}/booking", json=booking_payload, headers=headers)
    assert create_response.status_code == 200, f"Booking creation failed with status code {create_response.status_code}: {create_response.text}"
    booking_id = create_response.json().get("bookingid")

    # Get booking
    get_response = requests.get(f"{base_url}/booking/{booking_id}", headers=headers)
    assert get_response.status_code == 200, f"Failed to retrieve booking with status code {get_response.status_code}: {get_response.text}"

    # Update booking
    updated_payload = booking_payload.copy()
    updated_payload["additionalneeds"] = "Parking"
    update_response = requests.put(f"{base_url}/booking/{booking_id}", json=updated_payload, headers=headers)
    assert update_response.status_code == 200, f"Failed to update booking with status code {update_response.status_code}: {update_response.text}"

    # Delete booking
    delete_response = requests.delete(f"{base_url}/booking/{booking_id}", headers=headers)
    assert delete_response.status_code == 201, f"Failed to delete booking with status code {delete_response.status_code}: {delete_response.text}"