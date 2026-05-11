import os

drone_management_code = '''
class Drone:
    """
    Represents a drone model with its specifications.
    """
    def __init__(self, model_name, battery_capacity_wh):
        self.model_name = model_name
        self.battery_capacity_wh = battery_capacity_wh

    def get_battery_info(self):
        """
        Returns the battery capacity of the drone.
        """
        return f"{self.model_name} has a battery capacity of {self.battery_capacity_wh} Wh."

    def __str__(self):
        return f"Drone(Model: {self.model_name}, Battery Capacity: {self.battery_capacity_wh} Wh)"
'''

# Define the path for the new file
drone_management_file_path = os.path.join('src', 'drone_management.py')

# Write the Drone class code to the file
with open(drone_management_file_path, 'w') as f:
    f.write(drone_management_code)

print(f"Created {drone_management_file_path} with the Drone class.")

# Verify content
print(f"\n--- Content of {drone_management_file_path} ---")
with open(drone_management_file_path, 'r') as f:
    print(f.read())
