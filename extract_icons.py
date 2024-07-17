from PIL import Image
import os

# Load the image
sprite_image_path = './Minimap Icons.png'
sprite_image = Image.open(sprite_image_path)

# Set the dimensions of each icon
icon_width = 64  # Adjust based on the actual size of each icon in the sprite
icon_height = 64  # Adjust based on the actual size of each icon in the sprite

# Calculate the number of columns and rows
columns = sprite_image.width // icon_width
rows = sprite_image.height // icon_height

# Create a directory to save the individual icons
output_dir = './Extracted Icons'
os.makedirs(output_dir, exist_ok=True)

# Loop through each icon and save it as a separate image
for row in range(rows):
    for col in range(columns):
        left = col * icon_width
        upper = row * icon_height
        right = left + icon_width
        lower = upper + icon_height

        icon = sprite_image.crop((left, upper, right, lower))
        icon.save(os.path.join(output_dir, f'icon_{row}_{col}.png'))

print(f'Icons have been saved to {output_dir}')
