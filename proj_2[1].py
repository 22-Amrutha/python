
print("name:amrutha;usn:1AY24AI007;SECTION:M")
import re
import os

# Get regular expression pattern from user
pattern = input("Enter a regular expression to search for: ")
regex = re.compile(pattern)

# Get the folder path from the user (or use current directory)
folder = input("Enter the folder path to search in (leave blank for current directory): ")
if folder.strip() == '':
    folder = '.'

# Go through all .txt files in the folder
for filename in os.listdir(folder):
    if filename.endswith('.txt'):
        filepath = os.path.join(folder, filename)
        with open(filepath, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for i, line in enumerate(lines, 1):
                if regex.search(line):
                    print(f"{filename} (line {i}): {line.strip()}")