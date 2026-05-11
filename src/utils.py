import os

utils_code = '''
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches

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

def visualize_search_areas(sar_scenarios):
    fig, ax = plt.subplots(1, figsize=(10, 8))

    # Set map boundaries roughly based on typical Indian coordinates
    ax.set_xlim(68, 98)  # Longitude for India
    ax.set_ylim(8, 38)   # Latitude for India

    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.set_title("Simulated Search and Rescue Areas")
    ax.grid(True)

    for scenario in sar_scenarios:
        search_area = scenario['search_area']
        scenario_id = scenario['scenario_id']
        terrain = scenario['terrain_type']

        lat_min = search_area['lat_min']
        lat_max = search_area['lat_max']
        lon_min = search_area['lon_min']
        lon_max = search_area['lon_max']

        # Create a rectangle patch for the search area
        # width = lon_max - lon_min, height = lat_max - lat_min
        rect = patches.Rectangle((lon_min, lat_min), lon_max - lon_min, lat_max - lat_min,
                                 linewidth=1, edgecolor='r', facecolor='none',
                                 label=f'{scenario_id} ({terrain})')
        ax.add_patch(rect)

        # Add a text label for the scenario ID at the center of the rectangle
        ax.text(lon_min + (lon_max - lon_min) / 2, lat_min + (lat_max - lat_min) / 2,
                scenario_id, color='blue', fontsize=8, ha='center', va='center')

    ax.legend()
    plt.show()

def visualize_medical_locations(medical_data):
    fig, ax = plt.subplots(1, figsize=(10, 8))

    # Set map boundaries roughly based on typical Indian coordinates
    ax.set_xlim(68, 98)  # Longitude for India
    ax.set_ylim(8, 38)   # Latitude for India

    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.set_title("Simulated Medical Emergency Locations")
    ax.grid(True)

    lats = []
    lons = []
    labels = []

    for patient in medical_data:
        location_str = patient['location']
        # Parse location string (e.g., '21.6742 N, 77.368 E')
        parts = location_str.replace(' N,', '').replace(' E', '').split(' ')
        if len(parts) == 2:
            try:
                lat = float(parts[0])
                lon = float(parts[1])
                lats.append(lat)
                lons.append(lon)
                labels.append(patient['patient_id'])
            except ValueError:
                print(f"Could not parse location for {patient['patient_id']}: {location_str}")
                continue

    ax.scatter(lons, lats, color='red', s=100, alpha=0.7, edgecolors='black', label='Patient Locations')

    for i, txt in enumerate(labels):
        ax.annotate(txt, (lons[i], lats[i]), textcoords="offset points", xytext=(5,5), ha='center')

    ax.legend()
    plt.show()
'''

# Define the path for the new file
utils_file_path = os.path.join('src', 'utils.py')

# Write the utility code to the file
with open(utils_file_path, 'w') as f:
    f.write(utils_code)

print(f"Created {utils_file_path} with simulation and visualization utility functions.")

# Verify content
print(f"\n--- Content of {utils_file_path} ---")
with open(utils_file_path, 'r') as f:
    print(f.read())
