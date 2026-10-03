import json, pathlib

base = pathlib.Path(__file__).resolve().parent
BASE_URL = "https://raw.githubusercontent.com/elijahzins/chore-images/main"

data = [
    {"id": str(i), "image_url": f"{BASE_URL}/image_{i:03d}.jpg"}
    for i in range(1, 103)
]

with open(base / "data.json", "w") as f:
    json.dump(data, f, indent=4)

print(f"Wrote {len(data)} items")