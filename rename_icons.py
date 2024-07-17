import json
import os

# Load the metadata
metadata_file_path = './Minimap Icons Metadata.json'
with open(metadata_file_path, 'r') as file:
    metadata = json.load(file)

# Directory containing the extracted icons
extracted_icons_dir = './Extracted Icons'

# Loop through the metadata and rename each icon file
for index, data in enumerate(metadata):
    old_file_name = os.path.join(extracted_icons_dir, f'icon_{index // 14}_{index % 14}.png')
    new_file_name = os.path.join(extracted_icons_dir, f'{data["Id"]}.png')

    if os.path.exists(old_file_name):
        os.rename(old_file_name, new_file_name)
    else:
        # Handle missing files - since it's not gonna be NxN icons you'll
        # expect see a few 'not found' messages - that's ok!
        print(f'File not found: {old_file_name}')

print(f'Icons have been renamed based on the metadata in {metadata_file_path}')
