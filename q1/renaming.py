import os

folder_path = "q1\dataset\monkey"  # Replace this with the path to your folder
prefix = "monkey_"

# List all files in the folder
files = os.listdir(folder_path)

# Sort the files based on their names
files.sort()

# Iterate over the sorted files and rename them sequentially
for i, file_name in enumerate(files):
    _, extension = os.path.splitext(file_name)
    new_name = f"{prefix}{i+1}{extension}"
    os.rename(os.path.join(folder_path, file_name), os.path.join(folder_path, new_name))
