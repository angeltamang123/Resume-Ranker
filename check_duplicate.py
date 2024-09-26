import json

# Path to your JSON file
json_file_path = '/home/angel-tamang/Resume-Ranker/data/jd/web_developer.json'

# Load the JSON data from the file
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Dictionary to store unique items based on job name and company (or other fields)
unique_jobs = {}

# Check and filter duplicates
for key, value in data.items():
    if isinstance(value, list):  # Check if the value is a list (array)
        unique_list = []
        for job in value:
            # Create a unique key by combining job name and company
            unique_key = (job.get('name'), job.get('company'))
            if unique_key not in unique_jobs:
                unique_jobs[unique_key] = job
                unique_list.append(job)
        
        # Update the array with only unique items
        data[key] = unique_list
        print(f"After removing duplicates, '{key}' contains {len(unique_list)} unique items.")

# Save the updated JSON data back to the file
with open(json_file_path, 'w') as file:
    json.dump(data, file, indent=4)

print("Duplicates removed and JSON file updated.")
