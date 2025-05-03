from create_condition import create_condition

########################################################
# Update with your own values

#walker texas ranger
patient_id = 'd6136698-553b-4aa4-96b4-7841c67e3f14'

# patient_id = 'id_of_the_patient_you_want_to_create_a_condition_for'

########################################################

# Create Condition
result = create_condition(patient_id)
print(result)
