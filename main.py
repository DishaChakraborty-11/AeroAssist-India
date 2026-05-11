import os
import random
import subprocess

# The content to be written to main.py
main_py_content = '''
import random

from src.drone_management import Drone
from src.medical_response import handle_medical_emergency
from src.search_rescue import perform_search_and_rescue

def simulate_patient_data(num_patients=1):
    """
    Simulates medical emergency data for a given number of patients.
    Returns a list of dictionaries, each representing a patient\'s vital signs and location.
    """
    patients_data = []
    for i in range(num_patients):
        patient_id = f"P{i+1:03d}"
        heart_rate = random.randint(50, 180) # bpm
        blood_pressure_systolic = random.randint(90, 180) # mmHg
        blood_pressure_diastolic = random.randint(60, 120) # mmHg
        oxygen_saturation = random.randint(70, 100) # %SpO2
        temperature = round(random.uniform(35.0, 41.0), 1) # Celsius
        location_lat = round(random.uniform(20.0, 30.0), 4) # Example Indian latitude range
        location_lon = round(random.uniform(70.0, 80.0), 4) # Example Indian longitude range

        patients_data.append({
            "patient_id": patient_id,
            "heart_rate": heart_rate,
            "blood_pressure_systolic": blood_pressure_systolic,
            "blood_pressure_diastolic": blood_pressure_diastolic,
            "oxygen_saturation": oxygen_saturation,
            "temperature": temperature,
            "location": f"{location_lat} N, {location_lon} E"
        })
    return patients_data

def simulate_search_and_rescue_data(num_scenarios=1):
    """
    Simulates search and rescue scenarios.
    Returns a list of dictionaries, each representing a search area and details.
    """
    sar_scenarios = []
    for i in range(num_scenarios):
        scenario_id = f"SAR{i+1:03d}"
        # Define a search area
        lat_center = round(random.uniform(20.0, 30.0), 4) # Example Indian latitude range
        lon_center = round(random.uniform(70.0, 80.0), 4) # Example Indian longitude range

        # Create a bounding box around the center
        lat_min = round(lat_center - random.uniform(0.1, 0.5), 4)
        lat_max = round(lat_center + random.uniform(0.1, 0.5), 4)
        lon_min = round(lon_center - random.uniform(0.1, 0.5), 4)
        lon_max = round(lon_center + random.uniform(0.1, 0.5), 4)

        missing_persons_count = random.randint(1, 10)
        terrain_type = random.choice(["Dense Forest", "Mountainous", "Coastal", "Urban Rubble"])
        weather_conditions = random.choice(["Clear", "Rainy", "Foggy", "Windy"])
        last_seen_time = random.randint(1, 48) # hours ago

        # Add estimated flight distance and payload for battery calculation
        estimated_distance_km = round(random.uniform(5.0, 50.0), 1)
        payload_kg = round(random.uniform(0.1, 5.0), 1)

        sar_scenarios.append({
            "scenario_id": scenario_id,
            "search_area": {
                "lat_min": min(lat_min, lat_max),
                "lat_max": max(lat_min, lat_max),
                "lon_min": min(lon_min, lon_max),
                "lon_max": max(lon_min, lon_max)
            },
            "missing_persons_count": missing_persons_count,
            "terrain_type": terrain_type,
            "weather_conditions": weather_conditions,
            "last_seen_time_hours": last_seen_time,
            "estimated_distance_km": estimated_distance_km,
            "payload_kg": payload_kg
        })
    return sar_scenarios

# Generate some sample data for medical emergencies
simulated_medical_data = simulate_patient_data(num_patients=3)

# Generate some sample SAR data
simulated_sar_data = simulate_search_and_rescue_data(num_scenarios=2)


# Main execution block
if __name__ == "__main__":
    print("\\n--- Swadeshi for Atmanirbhar Bharat - Robotics and Drones Project ---")
    print("This is a foundational script. Let\\\'s build specific features!")

    # Example Usage for Medical Emergency Response with Simulated Data
    print("\\n--- Processing Simulated Medical Emergency Data ---")
    for patient_data in simulated_medical_data:
        handle_medical_emergency(patient_data)

    # Example Usage for Search and Rescue with Simulated Data
    print("\\n--- Processing Simulated Search and Rescue Scenarios ---")
    for scenario_data in simulated_sar_data:
        perform_search_and_rescue(scenario_data)

    print("\\nWhat would you like to work on next? Perhaps refining one of these functions, or adding another capability?")
'''

# Define the path for the new file
main_py_path = os.path.join('src', 'main.py')

# Write the main_py_content to the file
with open(main_py_path, 'w') as f:
    f.write(main_py_content)

print(f"Updated {main_py_path} with imports and data simulation functions.")

# Verify content
print(f"\n--- Content of {main_py_path} ---")
with open(main_py_path, 'r') as f:
    print(f.read())

# Finally, execute the main.py script to verify its functionality
print("\n--- Executing refactored main.py ---")
try:
    # Add the current directory to PYTHONPATH for subprocess to find 'src' package
    my_env = os.environ.copy()
    if 'PYTHONPATH' in my_env:
        my_env['PYTHONPATH'] = os.getcwd() + os.pathsep + my_env['PYTHONPATH']
    else:
        my_env['PYTHONPATH'] = os.getcwd()

    result = subprocess.run(['python', main_py_path], capture_output=True, text=True, check=True, env=my_env)
    print(result.stdout)
    if result.stderr:
        print("Error during main.py execution:")
        print(result.stderr)
except subprocess.CalledProcessError as e:
    print(f"Failed to execute main.py: {e}")
    print(f"Stdout: {e.stdout}")
    print(f"Stderr: {e.stderr}")
