import os

search_rescue_code = '''
import random

def perform_search_and_rescue(sar_scenario):
    """
    Enhanced function for search and rescue operations using drones.
    This involves:
    - Drone path planning for efficient area coverage.
    - Object detection (e.g., thermal imaging for survivors).
    - Communication with ground teams.
    - Delivering survival kits.
    - Battery consumption calculation.
    """
    scenario_id = sar_scenario.get('scenario_id', 'Unknown Scenario')
    search_area = sar_scenario.get('search_area', {})
    missing_persons = sar_scenario.get('missing_persons_count', 0)
    terrain = sar_scenario.get('terrain_type', 'Unknown')
    weather = sar_scenario.get('weather_conditions', 'Unknown')
    last_seen = sar_scenario.get('last_seen_time_hours', 0)
    estimated_distance_km = sar_scenario.get('estimated_distance_km', 10.0)
    payload_kg = sar_scenario.get('payload_kg', 0.5)

    print(f"\\n[Search & Rescue Operation for Scenario: {scenario_id}]")
    print(f"\\tSearch Area: Lat {search_area.get('lat_min')}-{search_area.get('lat_max')}, Lon {search_area.get('lon_min')}-{search_area.get('lon_max')}")
    print(f"\\tMissing Persons: {missing_persons}, Terrain: {terrain}, Weather: {weather}, Last Seen: {last_seen} hours ago")
    print(f"\\tEstimated Flight Distance: {estimated_distance_km} km, Payload: {payload_kg} kg")

    print("\\t--- Initiating Drone-based Search Strategy ---")
    drone_strategy = ""
    path_planning_details = ""
    operational_speed_factor = 1.0 # Multiplier for search speed
    detection_equipment = []

    # Battery consumption parameters (Wh/km and Wh/kg-km)
    BASE_CONSUMPTION_RATE_WH_KM = 5.0 # Example: 5 Wh per km for a light drone
    PAYLOAD_CONSUMPTION_RATE_WH_KG_KM = 2.0 # Example: additional 2 Wh per kg per km
    DRONE_BATTERY_CAPACITY_WH = 200.0 # Example: 200 Wh battery capacity

    if terrain == "Dense Forest":
        drone_strategy = "Employing vertical grid search pattern."
        path_planning_details = "Flight paths adjusted for tree canopy penetration and obstacle avoidance. Focus on small, agile drones."
        operational_speed_factor = 0.6
        detection_equipment.extend(["Thermal Camera", "LiDAR for terrain mapping"])
        recommended_actions = ["Deploy specialized forest-penetrating drones."]
    elif terrain == "Mountainous":
        drone_strategy = "Utilizing contour-following flight paths."
        path_planning_details = "Altitude and pitch constantly adjusted to follow mountain contours, ensuring consistent sensor coverage. Long-range communication essential."
        operational_speed_factor = 0.7
        detection_equipment.extend(["High-resolution Optical Camera", "Advanced GPS for elevation data"])
        recommended_actions = ["Prioritize stable drones with long-range communication."]
    elif terrain == "Urban Rubble":
        drone_strategy = "Executing close-quarters spiral search pattern."
        path_planning_details = "Intricate 3D mapping and collision avoidance critical for navigating debris and collapsed structures. Focus on void space detection."
        operational_speed_factor = 0.5
        detection_equipment.extend(["High-resolution Optical Camera", "Micro-drones for confined spaces"])
        recommended_actions = ["Deploy small, agile drones with obstacle avoidance and specialized cameras."]
    elif terrain == "Coastal":
        drone_strategy = "Wide-area sweep patterns over land and water."
        path_planning_details = "Consideration for wind patterns and sea state. Utilize amphibious drones if water search is primary. "
        operational_speed_factor = 0.9
        detection_equipment.extend(["Visible Light Camera", "Marine Radar"])
        recommended_actions = ["Use drones with good endurance and water-landing capabilities."]
    else:
        drone_strategy = "Standard grid search pattern."
        path_planning_details = "Systematic coverage of the defined search grid, optimizing for efficiency."
        operational_speed_factor = 1.0
        detection_equipment.extend(["Optical Camera", "Thermal Camera"])
        recommended_actions = ["Standard drone deployment with visual inspection."]

    if weather == "Foggy" or weather == "Rainy":
        drone_strategy += " Prioritizing radar and thermal imaging over optical for visibility."
        path_planning_details += " Weather-resistant drone selection and advanced navigation (e.g., RTK GPS) for precision are crucial."
        operational_speed_factor *= 0.8 # Reduce speed in bad weather
        if "Thermal Camera" not in detection_equipment: detection_equipment.append("Thermal Camera")
        if "Radar" not in detection_equipment: detection_equipment.append("Radar")
        recommended_actions.append("Ensure drones are weather-resistant and equipped with advanced navigation.")

    print(f"\\tStrategy: {drone_strategy}")
    print(f"\\tPath Planning: {path_planning_details}")
    print(f"\\tEstimated Search Speed Factor: {operational_speed_factor:.1f}x")
    print(f"\\tDetection Equipment: {", ".join(detection_equipment)}")

    # Calculate battery consumption
    total_battery_consumption_wh = (BASE_CONSUMPTION_RATE_WH_KM * estimated_distance_km) + \
                                   (PAYLOAD_CONSUMPTION_RATE_WH_KG_KM * payload_kg * estimated_distance_km)

    print(f"\\tCalculated Battery Consumption: {total_battery_consumption_wh:.2f} Wh")

    if total_battery_consumption_wh > DRONE_BATTERY_CAPACITY_WH:
        print(f"\\t*** ALERT: Insufficient battery capacity! Needed {total_battery_consumption_wh:.2f} Wh, but drone has {DRONE_BATTERY_CAPACITY_WH:.2f} Wh. ***")
        recommended_actions.append("Consider using a drone with larger battery capacity or planning for mid-mission battery swap/recharge.")

    # Simulate detection based on conditions
    detection_probability = 0.5 # Base probability
    if terrain == "Dense Forest": detection_probability -= 0.2
    if weather == "Foggy": detection_probability -= 0.3
    if missing_persons > 5: detection_probability += 0.1
    if last_seen > 24: detection_probability -= 0.1

    # Adjust detection probability based on speed factor
    detection_probability *= operational_speed_factor

    if random.random() < detection_probability:
        num_found = random.randint(1, missing_persons) if missing_persons > 0 else 0
        print(f"\\t*** ALERT: {num_found} potential survivor(s) detected! ***")
        recommended_actions.append(f"Dispatch ground teams to detected coordinates for verification. Prepare drone for delivering {random.choice(['first-aid kit', 'water', 'communication device'])}.")
        status_message = f"Search in {scenario_id} complete. {num_found} survivor(s) located. Ground teams dispatched."
    else:
        print("\\tNo immediate survivors detected. Continuing search operations.")
        status_message = f"Search in {scenario_id} ongoing. No survivors located yet."
        recommended_actions.append("Re-evaluate search parameters and consider deploying additional drones/resources.")

    print("\\tRecommended Actions:")
    for action in recommended_actions:
        print(f"\\t- {action}")

    return status_message
'''

# Define the path for the new file
search_rescue_file_path = os.path.join('src', 'search_rescue.py')

# Write the perform_search_and_rescue function code to the file
with open(search_rescue_file_path, 'w') as f:
    f.write(search_rescue_code)

print(f"Created {search_rescue_file_path} with the perform_search_and_rescue function.")

# Verify content
print(f"\n--- Content of {search_rescue_file_path} ---")
with open(search_rescue_file_path, 'r') as f:
    print(f.read())

# Now, regenerate and run main.py
import random

# Import refactored components
from src.drone_management import Drone
from src.medical_response import handle_medical_emergency
from src.search_rescue import perform_search_and_rescue

def simulate_patient_data(num_patients=1):
    """
    Simulates medical emergency data for a given number of patients.
    Returns a list of dictionaries, each representing a patient's vital signs and location.
    """
    patients_data = []
    for i in range(num_patients):
        patient_id = f"P{i+1:03d}" # This is an f-string to be evaluated later when main.py runs
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
            "location": f"{location_lat} N, {location_lon} E" # This is an f-string to be evaluated later when main.py runs
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
                "lat_min": min(lat_min, lat_max), # Ensure min/max are correct
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
    print("\n--- Swadeshi for Atmanirbhar Bharat - Robotics and Drones Project ---")
    print("This is a foundational script. Let's build specific features!")

    # Example Usage for Medical Emergency Response with Simulated Data
    print("\n--- Processing Simulated Medical Emergency Data ---")
    for patient_data in simulated_medical_data:
        handle_medical_emergency(patient_data)

    # Example Usage for Search and Rescue with Simulated Data
    print("\n--- Processing Simulated Search and Rescue Scenarios ---")
    for scenario_data in simulated_sar_data:
        perform_search_and_rescue(scenario_data)

    print("\nWhat would you like to work on next? Perhaps refining one of these functions, or adding another capability?")

# Write the updated content to main.py
main_py_path = os.path.join('src', 'main.py')
with open(main_py_path, 'w') as f:
    f.write('''
import random

from src.drone_management import Drone
from src.medical_response import handle_medical_emergency
from src.search_rescue import perform_search_and_rescue

def simulate_patient_data(num_patients=1):
    """
    Simulates medical emergency data for a given number of patients.
    Returns a list of dictionaries, each representing a patient's vital signs and location.
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
    print("\n--- Swadeshi for Atmanirbhar Bharat - Robotics and Drones Project ---")
    print("This is a foundational script. Let\'s build specific features!")

    # Example Usage for Medical Emergency Response with Simulated Data
    print("\n--- Processing Simulated Medical Emergency Data ---")
    for patient_data in simulated_medical_data:
        handle_medical_emergency(patient_data)

    # Example Usage for Search and Rescue with Simulated Data
    print("\n--- Processing Simulated Search and Rescue Scenarios ---")
    for scenario_data in simulated_sar_data:
        perform_search_and_rescue(scenario_data)

    print("\nWhat would you like to work on next? Perhaps refining one of these functions, or adding another capability?")

''')

print(f"Updated {main_py_path}.")

# Verify content
print(f"\n--- Content of {main_py_path} ---")
with open(main_py_path, 'r') as f:
    print(f.read())
