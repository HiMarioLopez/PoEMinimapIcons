from PIL import Image

# Load the image
sprite_image_path = '../Game Data/Minimap Icons.png'
sprite_image = Image.open(sprite_image_path)

# Get the dimensions of the sprite image
sprite_width, sprite_height = sprite_image.size

# Manually count the number of icons in one row and one column
num_columns = 14  # Adjust based on actual count
num_rows = 46  # Adjust based on actual count

# Calculate the width and height of each icon
icon_width = sprite_width // num_columns
icon_height = sprite_height // num_rows

print(f'Icon Width: {icon_width}, Icon Height: {icon_height}')
