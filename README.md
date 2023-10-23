# imte
A package for converting images to tensors and tensors to images.

# Image Processor

The Image Processor is a command-line tool that allows you to convert images to tensors and vice versa. It provides a simple and efficient way to manipulate image files.

## Features

- Convert images to tensors
- Convert tensors to images
- Remove files

## Requirements

- Python 3.11.5
- argparse library
- torchvision library
- torch library
- Pillow library

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/mehdee81/imte.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

The Image Processor provides the following command-line options:

- `-totensor`: Convert an image to a tensor.
   ```
   python imte.py -totensor "image name" -name "tensor file name"
   ```

- `-toimage`: Convert a tensor to an image.
   ```
   python imte.py -toimage "tensor file name" -name "image  name"
   ```

- `-rm`: Remove a file.
   ```
   python imte.py -rm <file_to_remove>
   ```

## Examples

Convert an image to a tensor:
   ```
   python imte.py -totensor "c.png" -name "image2"
   ```

Convert a tensor to an image:
   ```
   python imte.py -toimage "image2.pt" -name "image2"
   ```

Remove a file:
   ```
   python imte.py -rm "file_to_remove.jpg"
   ```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Contact

For any questions or inquiries, please contact [mehdee.m81@gmail.com](mailto:mehdee.m81@gmail.com).
