#1. Closing Gaps in Numbered Files (e.g., spam001.txt to spam002.txt)

import os
import re

def close_gaps(folder, prefix):
    files = os.listdir(folder)
    pattern = re.compile(rf"^{re.escape(prefix)}(\d+)\.txt$")

    # Match and collect numbered files
    numbered_files = []
    for filename in files:
        match = pattern.match(filename)
        if match:
            number = int(match.group(1))
            numbered_files.append((number, filename))

    # Sort files by their number
    numbered_files.sort()

    # Rename files to fill in gaps
    expected_number = 1
    for current_number, filename in numbered_files:
        if current_number != expected_number:
            new_name = f"{prefix}{str(expected_number).zfill(3)}.txt"
            print(f"Renaming {filename} -> {new_name}")
            os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))
        expected_number += 1

# Example usage
if __name__ == "__main__":
    folder = input("Enter folder path: ")
    prefix = input("Enter file prefix (e.g., 'spam'): ")
    close_gaps(folder, prefix)
#2. Inserting a Gap into Numbered Files (e.g., to insert spam003.txt)
import os
import re

def insert_gap(folder, prefix, insert_at):
    files = os.listdir(folder)
    pattern = re.compile(rf"^{re.escape(prefix)}(\d+)\.txt$")

    numbered_files = []
    for filename in files:
        match = pattern.match(filename)
        if match:
            number = int(match.group(1))
            numbered_files.append((number, filename))

    numbered_files.sort(reverse=True)  # Go backward to avoid overwriting

    for number, filename in numbered_files:
        if number >= insert_at:
            new_number = number + 1
            new_name = f"{prefix}{str(new_number).zfill(3)}.txt"
            print(f"Renaming {filename} -> {new_name}")
            os.rename(os.path.join(folder, filename), os.path.join(folder, new_name))

# Example usage
if __name__ == "__main__":
    folder = input("Enter folder path: ")
    prefix = input("Enter file prefix (e.g., 'spam'): ")
    insert_at = int(input("Insert gap at number: "))
    insert_gap(folder, prefix, insert_at)

