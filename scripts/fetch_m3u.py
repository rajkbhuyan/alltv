import os
import requests

# URL from GitHub secret
M3U_URL = os.getenv("M3U_URL")
if not M3U_URL:
    raise ValueError("M3U_URL environment variable not set!")

OUTPUT_FOLDER = "playlists"
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

# Fetch M3U
response = requests.get(M3U_URL, timeout=30)
if response.status_code != 200:
    raise ValueError(f"Failed to fetch M3U: {response.status_code}")

lines = response.text.splitlines()

# Split into smaller files (~50,000 lines each to stay <100MB)
MAX_LINES = 50000
for i in range(0, len(lines), MAX_LINES):
    part_number = i // MAX_LINES + 1
    chunk_file = os.path.join(OUTPUT_FOLDER, f"alltv_part{part_number}.m3u")
    with open(chunk_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines[i:i+MAX_LINES]))
    print(f"Saved {chunk_file} ({len(lines[i:i+MAX_LINES])} lines)")
