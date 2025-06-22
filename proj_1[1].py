
print("name:amrutha;usn:1AY24AI007;SECTION:M")
import re

# Read the template file
with open('madlibs_input.txt', 'r') as file:
    content = file.read()

# Find all placeholders like ADJECTIVE, NOUN, VERB, ADVERB
placeholders = re.findall(r'\b(ADJECTIVE|NOUN|ADVERB|VERB)\b', content)

# Replace each placeholder with user input
for word in placeholders:
    user_input = input(f"Enter a {word.lower()}: ")
    content = content.replace(word, user_input, 1)

# Print the result
print("\n--- Final Story ---\n")
print(content)

# Save to a new file
with open('madlibs_output.txt', 'w') as file:
    file.write(content)

print("\nThe story has been saved to 'madlibs_output.txt'")