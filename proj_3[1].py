print("name:amrutha;usn:1AY24AI007;SECTION:M")

import os
import shutil

def selective_copy(source_folder, dest_folder, file_ext):
    # Ensure destination folder exists
    os.makedirs(dest_folder, exist_ok=True)

    # Walk through the folder tree
    for foldername, subfolders, filenames in os.walk(source_folder):
        for filename in filenames:
            if filename.lower().endswith(file_ext.lower()):
                source_path = os.path.join(foldername, filename)
                dest_path = os.path.join(dest_folder, filename)
                print(f"Copying: {source_path} -> {dest_path}")
                shutil.copy2(source_path, dest_path)

# User input
source = input("Enter the source folder path: ")
destination = input("Enter the destination folder path: ")
extension = input("Enter the file extension (e.g., .pdf, .jpg): ")

# Call the function
selective_copy(source, destination, extension)