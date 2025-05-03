import requests
from datetime import date
import os

########################################################
# Update with your own bearer token generated from auth.sh
# bearer_token = "your_bearer_token_here"
bearer_token = os.getenv('MEDPLUM_BEARER_TOKEN')

base_url = "https://api.medplum.com/fhir/R4/"
condition_url = base_url.rstrip('/') + '/Condition'


def create_condition(patient_id):
    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Content-Type': 'application/json'
    }
    payload = {
        "category": [{
            "coding": [{
                "code":
                "encounter-diagnosis",
                "system":
                "http://terminology.hl7.org/CodeSystem/condition-category"
            }]
        }],
        "clinicalStatus": {
            "coding": [{
                "code":
                "active",
                "system":
                "http://terminology.hl7.org/CodeSystem/condition-clinical"
            }]
        },
        "code": {
            "coding": [{
                "code": "J45.51",
                "display":
                "Severe persistent asthma with (acute) exacerbation",
                "system": "http://hl7.org/fhir/sid/icd-10-cm"
            }]
        },
        "resourceType":
        "Condition",
        "subject": {
            "reference": f"Patient/{patient_id}"
        },
        "verificationStatus": {
            "coding": [{
                "code":
                "confirmed",
                "system":
                "http://terminology.hl7.org/CodeSystem/condition-ver-status"
            }]
        }
    }
    response = requests.post(condition_url, headers=headers, json=payload)

    # Optionally, inspect the response
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
