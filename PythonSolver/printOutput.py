import numpy as np

# File path
file_path = "./output/output_sample_file_4.npz"

# Load the .npz file
loaded_data = np.load(file_path)

# Access and print all arrays in the file
for key in loaded_data:
    print(f"Array name: {key}")
    print(loaded_data[key])
    print("---") 