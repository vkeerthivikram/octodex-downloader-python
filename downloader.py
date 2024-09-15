import requests
from bs4 import BeautifulSoup
import os

# Create a directory to save images
os.makedirs('octodex_images', exist_ok=True)

# URL of the Octodex page
url = 'https://octodex.github.com/'

# Send a GET request to the URL
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find all image elements
images = soup.find_all('img')

# Loop through each image and download it
for img in images:
    if 'data-src' in img.attrs:
        img_url = img['data-src']
        
        # Ensure the URL is complete
        if not img_url.startswith('http'):
            img_url = 'https://octodex.github.com' + img_url  # Prepend the base URL

        print(f"Attempting to download from URL: {img_url}")  # Print the URL

        img_name = img['alt'] + '.png'  # Use the alt text as the filename
        img_path = os.path.join('octodex_images', img_name)

        # Check if the image is already downloaded
        if os.path.exists(img_path):
            print(f"{img_name} already downloaded.")
        else:
            print(f"Downloading {img_name}...")
            # Download the image
            img_response = requests.get(img_url)
            
            # Check if the download was successful
            if img_response.status_code == 200:
                # Save the image
                with open(img_path, 'wb') as f:
                    f.write(img_response.content)
                print(f"{img_name} downloaded successfully!")
            else:
                print(f"Failed to download {img_name}. Status code: {img_response.status_code}")
    else:
        print(f"Skipping image without 'data-src' attribute.")

print("All images processed.")