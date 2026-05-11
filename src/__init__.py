import os

# Define the source directory path
src_dir = 'src'

# Create the src directory if it doesn't exist
os.makedirs(src_dir, exist_ok=True)
print(f"Ensured directory exists: {src_dir}/")

# Create an empty __init__.py file inside the src directory
init_file_path = os.path.join(src_dir, '__init__.py')
with open(init_file_path, 'w') as f:
    pass # Create an empty file
print(f"Created empty file: {init_file_path}")
