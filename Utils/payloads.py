def valid_booking_payload():
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
def updated_booking_payload():
    return {
        "firstname": "Ariana",
        "lastname": "Grande", 
        "totalprice": 250,
        "depositpaid": False,
        "bookingdates": {
            "checkin": "2018-03-01",
            "checkout": "2018-04-01"
        },
        "additionalneeds": "Parking"
    }


def invalid_booking_payload_missing_firstname():
    return {
        "lastname": "James",
        "totalprice": 200,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2018-02-01"
        },
        "additionalneeds": "Breakfast"
    }

def invalid_booking_payload_bad_price():
    payload = valid_booking_payload()
    payload["totalprice"] = "Hundred"
    return payload

def invalid_booking_payload_bad_dates():
    payload = valid_booking_payload()
    payload["bookingdates"] = {
        "checkin": "2019-01-01",
        "checkout": "2018-01-01"
    }
    return payload