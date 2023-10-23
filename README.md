# imve
A package for converting images to vectors and vectors to images.

# Image Processor

The Image Processor is a command-line tool that allows you to convert images to vectors and vice versa. It provides a simple and efficient way to manipulate image files.

## Features

- Convert images to vectors
- Convert vectors to images
- Remove files

## Requirements

- Python 3.11.5
- argparse library
- torchvision

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/mehdee81/imve.git
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

The Image Processor provides the following command-line options:

- `-tovector`: Convert an image to a vector.
   ```
   python imve.py -tovector <image_file>
   ```

- `-toimage`: Convert a vector to an image.
   ```
   python imve.py -toimage <vector>
   ```

- `-rm`: Remove a file.
   ```
   python imve.py -rm <file_to_remove>
   ```

## Examples

- Convert an image to a vector:
   ```
   python imve.py -tovector "image.jpg"
   ```

- Convert a vector to an image:
   ```
   python imve.py -toimage vector
   ```

- Remove a file:
   ```
   python imve.py -rm "file_to_remove.jpg"
   ```

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## Contact

For any questions or inquiries, please contact [mehdee.m81@gmail.com](mailto:mehdee.m81@gmail.com).
