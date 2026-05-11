import os

medical_response_code = '''
def handle_medical_emergency(patient_data):
    """
    Enhanced function for handling medical emergencies based on vital signs.
    This could involve:
    - Receiving vital signs from sensors.
    - Analyzing data for critical conditions.
    - Deploying medical supplies via drone.
    - Alerting emergency services.
    """
    patient_id = patient_data.get('patient_id', 'Unknown Patient')
    heart_rate = patient_data.get('heart_rate')
    oxygen_saturation = patient_data.get('oxygen_saturation')
    bp_systolic = patient_data.get('blood_pressure_systolic')
    bp_diastolic = patient_data.get('blood_pressure_diastolic')
    temperature = patient_data.get('temperature')
    location = patient_data.get('location', 'Unknown Location')

    print(f"\n[Medical Emergency Handler for {patient_id}]")
    print(f"\tLocation: {location}")
    print(f"\tVitals: HR={heart_rate} bpm, SpO2={oxygen_saturation}%, BP={bp_systolic}/{bp_diastolic} mmHg, Temp={temperature}°C")

    emergency_detected = False
    recommended_actions = []

    # Heart Rate Conditions
    if heart_rate:
        if heart_rate > 150:
            emergency_detected = True
            recommended_actions.append("Critical Tachycardia detected. Prepare AED and notify advanced life support.")
        elif heart_rate > 100:
            emergency_detected = True
            recommended_actions.append("Tachycardia detected. Assess for underlying cause. Prepare AED.")
        elif heart_rate < 40:
            emergency_detected = True
            recommended_actions.append("Critical Bradycardia detected. Prepare for cardiac support and notify advanced life support.")
        elif heart_rate < 60:
            emergency_detected = True
            recommended_actions.append("Bradycardia detected. Monitor rhythm and perfusion.")

    # Oxygen Saturation Conditions
    if oxygen_saturation:
        if oxygen_saturation < 80:
            emergency_detected = True
            recommended_actions.append("Severe Hypoxia detected. Initiate high-flow oxygen and prepare for intubation.")
        elif oxygen_saturation < 90:
            emergency_detected = True
            recommended_actions.append("Hypoxia detected. Administer oxygen. Monitor respiratory effort.")

    # Blood Pressure Conditions
    if bp_systolic and bp_diastolic:
        if bp_systolic < 70:
            emergency_detected = True
            recommended_actions.append("Hypotensive Shock detected. Initiate fluid resuscitation and vasopressors. Drone dispatch for IV fluids.")
        elif bp_systolic < 90:
            emergency_detected = True
            recommended_actions.append("Hypotension detected. Monitor for signs of shock. Consider fluid bolus.")
        elif bp_systolic > 180 or bp_diastolic > 120:
            emergency_detected = True
            recommended_actions.append("Hypertensive Crisis detected. Administer antihypertensives. Drone dispatch for medication.")
        elif bp_systolic > 140 or bp_diastolic > 90:
            emergency_detected = True
            recommended_actions.append("Hypertension detected. Monitor and consider medication if sustained.")

    # Temperature Conditions
    if temperature:
        if temperature > 40.0:
            emergency_detected = True
            recommended_actions.append("Severe Hyperthermia. Implement aggressive cooling measures. Drone dispatch for cooling packs.")
        elif temperature > 38.5:
            emergency_detected = True
            recommended_actions.append("Fever detected. Administer antipyretics and monitor for infection.")
        elif temperature < 32.0:
            emergency_detected = True
            recommended_actions.append("Severe Hypothermia. Initiate rewarming protocols. Drone dispatch for warming blankets.")
        elif temperature < 35.0:
            emergency_detected = True
            recommended_actions.append("Hypothermia detected. Initiate passive rewarming.")

    if emergency_detected:
        print("\t--- *** CRITICAL EMERGENCY DETECTED *** ---")
        print("\tInitiating priority drone dispatch for essential medical supplies and equipment.")
        print("\tImmediately alerting nearest emergency services and specialized medical personnel.")
        for action in recommended_actions:
            print(f"\tAction: {action}")
        return f"Emergency for {patient_id} critically handled. Drone en route to {location} with priority."
    else:
        print("\tPatient vitals are within normal ranges. Continuous monitoring advised.")
        return f"No immediate critical emergency for {patient_id}. Monitoring ongoing."
'''

# Define the path for the new file
medical_response_file_path = os.path.join('src', 'medical_response.py')

# Write the handle_medical_emergency function code to the file
with open(medical_response_file_path, 'w') as f:
    f.write(medical_response_code)

print(f"Created {medical_response_file_path} with the handle_medical_emergency function.")

# Verify content
print(f"\n--- Content of {medical_response_file_path} ---")
with open(medical_response_file_path, 'r') as f:
    print(f.read())
