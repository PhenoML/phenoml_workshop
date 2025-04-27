from create_patient import create_patient0
import os

########################################################
# Update with your own values

first_name = "FirstName"
last_name = "LastName"
age = 28
sex = "M"
gender = "male"

########################################################
# Create patient
payload = create_patient0(first_name, last_name, age, sex, gender)
print(payload)

########################################################

