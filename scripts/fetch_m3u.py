import os
import requests

# Get URL from GitHub secret
M3U_URL = os.getenv("M3U_URL")
if not M3U_URL:
    raise ValueError("M3U_URL environment variable not set!")

# Output folder and file
OUTPUT_FOLDER = "playlists"
OUTPUT_FILE = os.path.join(OUTPUT_FOLDER, "alltv.m3u")

# Create folder if it doesn't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Fetch the raw M3U data
response = requests.get(M3U_URL, timeout=30)

if response.status_code == 200:
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(response.text)
    print("Raw M3U playlist saved successfully.")
else:
    print("Failed to fetch M3U:", response.status_code)
