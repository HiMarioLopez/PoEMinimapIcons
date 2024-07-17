# PoE Minimap Icons (+ Extraction Scripts)

![Icons Preview](./Icons%20Preview.png)

This repository contains all current minimap icons for Path of Exile in the `Extracted Icons` directory.

I've also included the Python script that extracts individual icons from the 'source' sprite image (found in the game data `art/2dart/minimap/player.png`). The script uses the Pillow library to split the sprite image into individual icon files based on the specified number of rows and columns.

## Features

- Load a sprite image containing multiple icons.
- Automatically calculate the dimensions of each icon.
- Split the sprite image into individual icon files.
- Save the extracted icons to a specified directory.
- Rename extracted icons based on metadata.

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

## Disclaimer

I do not own the icons themselves. The icons are the property of [Grinding Gear Games](https://www.grindinggear.com/). Use them responsibly.

## Acknowledgements

- [Grinding Gear Games](https://www.grindinggear.com/) - The creators and owners of the icon assets.
- zao (from the ['official' Path of Exile discord](https://discord.com/invite/pathofexile)) - The kind soul who provided me the source files.

## License

The code included in the `Scripts` directory is licensed under the MIT License.

```markdown
MIT License

Copyright (c) 2024 Mario Lopez Martinez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
