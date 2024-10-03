# Apple CleanUP Watermark remover

## Overview

The **Image Metadata Removal Module** is a Python package designed to remove specific metadata fields from image files, specifically focusing on eliminating the Apple AI cleanup logo/watermark. This can be useful for enhancing privacy, preparing images for distribution without identifying marks, or simply improving the aesthetics of an image without sacrificing its quality and colors. The module primarily targets JPEG images, which commonly contain EXIF metadata.

## Features

- Remove the Apple AI cleanup logo/watermark from JPEG images.
- Maintain original image quality and colors during the process.
- Built using Object-Oriented Programming (OOP) principles.
- Easily extensible for additional metadata fields or image formats.

## Project Structure

```
image_metadata_removal/
│
├── image_metadata_removal/
│   ├── __init__.py
│   ├── metadata_remover.py
│   ├── abc_metadata_remover.py
│
├── tests/
│   ├── __init__.py
│   ├── test_metadata_remover.py
│
├── requirements.txt
└── README.md
```

## Installation

### Install from Source

To install the package from source globally, follow these steps:

1. **Clone the repository**:
   ```
   git clone https://github.com/0x0060/apple_cleanup_remover.git
   cd apple_cleanup_remover
   ```

2. **Install the required packages**:
   ```
   pip install -r requirements.txt
   ```

3. **Install the package globally**:
   ```
   python setup.py install
   ```


## Usage

To use the module, follow these steps:

1. **Import the `MetadataRemover` class.**
2. **Create an instance of the `MetadataRemover`.**
3. **Call the `remove_metadata` method, providing the input and output file paths.**

Here is an example:

```py
from apple_cleanup_remover.metadata_remover import MetadataRemover

# Create an instance of MetadataRemover
remover = MetadataRemover()

# Specify the input and output image paths
input_image_path = 'input_image.jpg'
output_image_path = 'output_image.jpg'

# Remove metadata from the image
remover.remove_metadata(input_image_path, output_image_path)

print(f"Metadata removed and saved to {output_image_path}.")
```

### Supported Metadata Fields

The following metadata fields will be removed from the image:

- CurrentlPTCDigest
- CodedCharacterSet
- ApplicationRecordVersion
- DigitalCreationTime
- DigitalCreationDate
- Credit
- DateCreated
- TimeCreated
- IPTCDigest
- XMPT001kit
- CreatorTool
- DigitalSourceType
- DateTimeCreated
- DigitalCreationDateTime

## Testing

The module includes a set of unit tests to verify its functionality. To run the tests, make sure you have a test image file named `test_image.jpg` in the root directory of the project.

Run the tests using the following command:

```bash
python -m unittest discover tests/
```

## Contributing

Contributions are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch and create a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any inquiries or issues, please contact [ME](https://0x0060.dev/contact/).
