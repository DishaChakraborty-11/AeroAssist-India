
import random

from src.drone_management import Drone
from src.medical_response import handle_medical_emergency
from src.search_rescue import perform_search_and_rescue
from src.utils import simulate_patient_data, simulate_search_and_rescue_data, visualize_medical_locations, visualize_search_areas

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

    # Visualize medical locations
    print("\n--- Visualizing Medical Emergency Locations ---")
    visualize_medical_locations(simulated_medical_data)

    # Example Usage for Search and Rescue with Simulated Data
    print("\n--- Processing Simulated Search and Rescue Scenarios ---")
    for scenario_data in simulated_sar_data:
        perform_search_and_rescue(scenario_data)

    # Visualize search areas
    print("\n--- Visualizing Search and Rescue Areas ---")
    visualize_search_areas(simulated_sar_data)
