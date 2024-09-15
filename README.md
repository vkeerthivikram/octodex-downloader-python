# Octodex Downloader

A Python script for effortlessly downloading images from the Octodex website.

## Features

- **Image Downloading**: Downloads Octodex images that have the `data-src` attribute.
- **Smart Skipping**: Automatically skips images without the required attribute.
- **Error Handling**: Ensures image URLs are valid to avoid download errors.

## Requirements

To run this project, you'll need:

- Python 3.x
- Requests library
- BeautifulSoup4 library

## Installation

Follow these steps to get the project up and running:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/octodex-downloader-python.git
   ```
2. **Navigate to the project directory**:
   ```bash
   cd octodex-downloader-python
   ```
3. **Install the required packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To download images, simply run the script:

```bash
python downloader.py
```

The script will create an `octodex_images` directory and save all downloaded images there.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to enhance the project.

## License

This project is licensed under the MIT License.
