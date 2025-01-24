import os
import shutil

# Define the folder paths
source_folder = "photoshoot"  # Folder where the files with names like DSC0* are located
destination_folder = "shortlisted-photos"  # Folder where matching files will be moved
notepad_file = "shortlist.txt"  # Path to the notepad file containing the numbers

# Ensure the destination folder exists
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Read numbers from the notepad file
with open(notepad_file, 'r') as file:
    numbers = file.readlines()

# Clean up the numbers (remove any extra whitespace or newlines)
numbers = [num.strip() for num in numbers]

# Iterate over each number in the list
for number in numbers:
    # Build the search pattern (e.g., DSC0[number])
    if len(number)==3:
        pattern = f"DSC00{number}"
    elif len(number) == 4:
        pattern = f"DSC0{number}" 

    # List all files in the source folder
    for filename in os.listdir(source_folder):
        # Check if the file matches the pattern
        if filename.startswith(pattern):
            # Construct the full path of the file
            file_path = os.path.join(source_folder, filename)
            destination_path = os.path.join(destination_folder, filename)

            # Copy the file to the "shortlisted" folder
            try:
                shutil.copy(file_path, destination_path)
                print(f"Copied {filename} to {destination_folder}")
            except Exception as e:
                print(f"Error copying {filename}: {e}")

print("File moving process completed.")