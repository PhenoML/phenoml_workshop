from create_condition import create_condition

########################################################
# Update with your own values

#walker texas ranger
medplum_patient_id = 'd6136698-553b-4aa4-96b4-7841c67e3f14'

#select patient ID for the patient we created in the prior step
# canvas
canvas_patient_id = '77a9ac1d7ce04b17b99f683ba8f9361a'

########################################################

# Create Condition using language

text = "Patient has heart arrhythmia"

#Medplum
medplum_result = create_condition(medplum_patient_id, text, "medplum")
print(medplum_result)

# #Canvas
canvas_result = create_condition(canvas_patient_id, text, "canvas")
print(canvas_result)

