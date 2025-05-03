import requests
from datetime import date
import os

########################################################
# Update with your own bearer token generated from auth.sh
# bearer_token = "your_bearer_token_here"
phenoml_bearer_token = os.getenv('PHENOML_BEARER_TOKEN')
canvas_bearer_token = os.getenv('CANVAS_BEARER_TOKEN')
medplum_bearer_token = os.getenv('MEDPLUM_BEARER_TOKEN')

phenoml_url = "https://experiment-test.app.pheno.ml/lang2fhir/create"
canvas_condition_url = "https://fumage-xpc-dev.canvasmedical.com/Condition"
medplum_condition_url = "https://api.medplum.com/fhir/R4/Condition"


def create_condition(patient_id, text, fhir_api):
    phenoml_headers = {
        'Authorization': f'Bearer {phenoml_bearer_token}',
        'Content-Type': 'application/json'
    }

    text_payload = {
        "version": "R4",
        "resource": "condition-encounter-diagnosis",
        "text": text
    }

    phenoml_response = requests.post(phenoml_url,
                                     headers=phenoml_headers,
                                     json=text_payload)
    phenoml_json = phenoml_response.json()

    phenoml_json["subject"]["reference"] = f"Patient/{patient_id}"
    phenoml_json["subject"]["display"] = f"Patient/{patient_id}"

    if fhir_api == "canvas":
        fhir_api_bearer_token = canvas_bearer_token
        fhir_api_condition_url = canvas_condition_url
    elif fhir_api == "medplum":
        fhir_api_bearer_token = medplum_bearer_token
        fhir_api_condition_url = medplum_condition_url
    else:
        raise ValueError(f"Invalid FHIR API: {fhir_api}")

    headers = {
        'Authorization': f'Bearer {fhir_api_bearer_token}',
        'Content-Type': 'application/json'
    }

    response = requests.post(fhir_api_condition_url,
                             headers=headers,
                             json=phenoml_json)

    # Optionally, inspect the response
    print("Status Code:", response.status_code)
    print("Response Body:", response.text)
