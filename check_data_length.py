import json

# Path to your JSON file
json_file_path = '/home/angel-tamang/Resume-Ranker/data/jd/web_developer.json'

# Load the JSON data from the file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Loop through the keys and count the number of items if the value is a list
for key, value in data.items():
    if isinstance(value, list):  # Check if the value is an array
        print(f"Array '{key}' contains {len(value)} items.")
