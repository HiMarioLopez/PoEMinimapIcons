# PoE Minimap Icons (+ Extraction Scripts)

This repository contains all current minimap icons for Path of Exile in the `Extracted Icons` directory.

I've also included the Python script that extracts individual icons from the 'source' sprite image (found in the game data `art/2dart/minimap/player.png`). The script uses the Pillow library to split the sprite image into individual icon files based on the specified number of rows and columns.

## Features

- Load a sprite image containing multiple icons.
- Automatically calculate the dimensions of each icon.
- Split the sprite image into individual icon files.
- Save the extracted icons to a specified directory.

## Requirements

- Python 3.x
- Pillow library

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/HiMarioLopez/PoEMinimapIcons.git
   cd PoEMinimapIcons
   ```

2. Install the required dependencies:

   ```bash
    pip install pillow
   ```

## Usage

1. If you have an updated sprite sheet (these tend to get updated from league to league), place your updated sprite image in the project directory and name it `Minimap Icons.png`. Same for the `Minimap Icons Metadata.json`.

1. Edit the `calculate_icon_size.py` script to update the number of icons per row and column based on your updated sprite sheet:

    ```python
    # Manually count the number of icons in one row and one column
    num_columns = 14  # Adjust based on actual count
    num_rows = 46  # Adjust based on actual count
    ```

1. The script will run a calculation based on the sprite sheet's size, as well as the number of rows and columns - we should receive output that looks something like this

    ```text
    Icon Width: 64, Icon Height: 63
    ```

1. Rounding to a neater figure (power of 2s are cool), I update the values in my `extract_icons.py` script:

    ```python
    # Set the dimensions of each icon
    icon_width = 64  # Adjust based on the actual size of each icon in the sprite
    icon_height = 64  # Adjust based on the actual size of each icon in the sprite
    ```

1. Run the updated `extract_icons.py` Python script:

    ```bash
    python extract_icons.py
    ```

1. The extracted icons will be saved in the `Extracted Icons` directory.

1. Run the `rename_icons.py` script to map the `Minimap Icons Metadata.json` to the generated images.

## Contributing

Contributions are welcome! If you have an updated set of icons for future leagues, please submit a pull request. The latest batch is from the 3.24: Necropolis patch.
