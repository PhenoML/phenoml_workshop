from get_patient import search_patients

########################################################
# Update with your own values

age = 30  # optional
# gender = "male"  # "male", "female", or None
gender = None
########################################################
# Search for patients
result = search_patients(age=age, gender=gender)

# Show results
if result:
  entries = result.get('entry', [])
  print(f"Found {len(entries)} patient(s).")
  for entry in entries:
    patient = entry['resource']
    print(
        f"Patient ID: {patient.get('id')}, Name: {patient.get('name', [{}])[0].get('given', [''])[0]} {patient.get('name', [{}])[0].get('family', '')}, Gender: {patient.get('gender')}, Birthdate: {patient.get('birthDate')}"
    )
else:
  print("No patients found.")
