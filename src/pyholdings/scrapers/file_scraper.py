import requests
from pathlib import Path

def path_builder(path):
    dirs = path.split("/")[:-1]
    if dirs:
        Path(dirs).mkdir(parents=True, exist_ok=True)

def file_scraper(url, output_file_path, output_file_ext):
    path_builder(output_file_path)
    content = requests.get(url).content
    with open(f"scraped_data/{output_file_path}.{output_file_ext}", 'wb') as file:
        file.write(content)
