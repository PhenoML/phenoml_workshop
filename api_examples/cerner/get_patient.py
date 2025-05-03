# get_patient.py

import requests
from datetime import date, timedelta

# Base URL for Cerner sandbox
CERNER_BASE_FHIR_URL = 'https://fhir-open.cerner.com/r4/ec2458f2-1e24-41c8-b71b-0e701af7583d/Patient'


def search_patients(first_name=None, last_name=None, age=None, gender=None):
    """Search for patients by name, age, and/or gender."""

    today = date.today()
    params = []

    if first_name:
        params.append(f"given={first_name}")
    if last_name:
        params.append(f"family={last_name}")

    if age is not None:
        birthdate_from = (today.replace(year=today.year - age - 1) +
                          timedelta(days=1)).isoformat()
        birthdate_to = (today.replace(year=today.year - age)).isoformat()
        params.append(f"birthdate=ge{birthdate_from}")
        params.append(f"birthdate=le{birthdate_to}")

    if gender:
        params.append(f"gender={gender.lower()}")

    query_string = "&".join(params)
    url = f"{CERNER_BASE_FHIR_URL}?{query_string}" if query_string else CERNER_BASE_FHIR_URL

    print(f"Requesting: {url}")

    response = requests.get(url, headers={"Accept": "application/fhir+json"})
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return None
