import requests
from datetime import date
import os

########################################################
# Update with your own bearer token generated from auth.sh
# bearer_token = "your_bearer_token_here"
bearer_token = os.getenv('CANVAS_BEARER_TOKEN')

base_url = "https://fumage-xpc-dev.canvasmedical.com"
patient_url = base_url.rstrip('/') + '/Patient'


def age_to_iso_birthday_fixed(age):
    year = date.today().year - age
    approx_birthday = date(year, 1, 1)  # Always January 1
    return approx_birthday.isoformat()


def create_patient0(firstname, lastname, age, sex, gender):
    if sex not in ("F", "M", "OTH", "UNK"):
        raise ValueError(f"Sex {sex} is invalid")
    if gender not in ("female", "male", "other", "unknown"):
        raise ValueError(f"Gender {gender} is invalid")
    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Content-Type': 'application/json'
    }
    payload = {
        "resourceType":
        "Patient",
        "extension": [{
            "url":
            "http://hl7.org/fhir/us/core/StructureDefinition/us-core-birthsex",
            "valueCode": sex
        }],
        "gender":
        gender,
        "active":
        True,
        "name": [{
            "use": "official",
            "family": lastname,
            "given": [firstname]
        }],
        "birthDate":
        age_to_iso_birthday_fixed(age)
    }
    response = requests.post(patient_url, headers=headers, json=payload)

    # Optionally, inspect the response
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
