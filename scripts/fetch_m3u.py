import os
import requests

# Get URL from GitHub secret
M3U_URL = os.getenv("M3U_URL")
if not M3U_URL:
    raise ValueError("M3U_URL environment variable not set!")

# Where to save raw text
OUTPUT_FILE = "playlists/alltv.m3u"

response = requests.get(M3U_URL, timeout=30)

if response.status_code == 200:
    # Save raw text exactly as received
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(response.text)
    print("Raw M3U playlist saved successfully.")
else:
    print("Failed to fetch M3U:", response.status_code)
