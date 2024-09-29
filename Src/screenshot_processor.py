# screenshot_processor.py

import requests  # Used for making API calls to Pinata
from PIL import ImageGrab
import hashlib
import os
from datetime import datetime
import json

# Pinata API credentials (replace with your own)
PINATA_API_KEY = '606bf7408333ac6cbb86'
PINATA_SECRET_API_KEY = '7db80593754fe44568a684e2af1c4f23868132f3f78637e14d579b9f2e451c1c'

class ScreenshotProcessor:
    def __init__(self, file_path="snip_screenshot.png"):
        self.file_path = file_path

    def save_screenshot(self, bbox):
        """ Capture and save the screenshot within the selected bounding box. """
        screenshot = ImageGrab.grab(bbox=bbox)  # Use PIL to grab the image
        screenshot.save(self.file_path)
        print(f"Screenshot saved to {self.file_path}")
        return self.file_path

    def hash_screenshot(self):
        """ Generate a SHA-256 hash of the screenshot. """
        with open(self.file_path, "rb") as f:
            file_bytes = f.read()
            file_hash = hashlib.sha256(file_bytes).hexdigest()
        print(f"Screenshot Hash: {file_hash}")
        return file_hash

    def store_to_ipfs(self):
        """ Upload the screenshot to Pinata (IPFS) with date-time metadata. """
        url = "https://api.pinata.cloud/pinning/pinFileToIPFS"

        # Get the current date and time
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Metadata to attach to the file
        pinata_metadata = {
            "name": os.path.basename(self.file_path),  # File name as the metadata name
            "keyvalues": {
                "date_time": current_datetime  # Custom metadata field for date and time
            }
        }

        # Open the image file to send it in the request
        with open(self.file_path, 'rb') as file:
            files = {
                'file': (os.path.basename(self.file_path), file)
            }
            headers = {
                'pinata_api_key': PINATA_API_KEY,
                'pinata_secret_api_key': PINATA_SECRET_API_KEY
            }

            # Send POST request with metadata and file
            response = requests.post(url, files=files, headers=headers, data={
                'pinataMetadata': json.dumps(pinata_metadata)
            })

        if response.status_code == 200:
            ipfs_hash = response.json()['IpfsHash']
            print(f"File uploaded to IPFS with metadata. IPFS Hash: {ipfs_hash}")
            return ipfs_hash
        else:
            print(f"Failed to upload file with metadata: {response.status_code} {response.text}")
            return None