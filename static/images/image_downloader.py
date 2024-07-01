import os
import requests

image_url = "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/FT4GU4M.png"

destination_dir = os.path.expanduser("~/2web/static/images")

os.makedirs(destination_dir, exist_ok=True)

response = requests.get(image_url)
if response.status_code == 200:
    image_path = os.path.join(destination_dir, "rivendell.png")
    with open(image_path, 'wb') as file:
        file.write(response.content)
    print(f"Image downloaded and saved to {image_path}")
else:
    print("Failed to download the image. Status code:", response.status_code)