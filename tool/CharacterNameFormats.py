import re

# Read the file
file_path = 'D:\\Documents\\GitHub\\Test\\common\\characters\\CHI_Fate_Characters.txt'

def format_name(name):
    words = re.findall(r'\w+', name)
    formatted_name = words[0].upper() + "".join(w.capitalize() for w in words[1:])
    return formatted_name

# Load the characters data
with open(file_path, "r", encoding="utf-8") as file:
    characters_data = file.read()

# Define a regular expression pattern to match character names
pattern = r'name\s*=\s*("[^"]+"|[^,\n]+)'

# Find and format character names using regular expressions
formatted_data = re.sub(pattern, lambda match: f'name = "{format_name(match.group(1))}"', characters_data)

# Rewrite the original file with the updated data
with open(file_path, "w", encoding="utf-8") as file:
    file.write(formatted_data)

print("Character names formatted and saved in 'updated_characters_data.txt'.")