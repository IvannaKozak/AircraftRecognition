import json
import os

# Load Kaggle API credentials
with open("kaggle.json", "r") as file:
    credentials = json.load(file)

os.environ['KAGGLE_USERNAME'] = credentials['username']
os.environ['KAGGLE_KEY'] = credentials['key']


import subprocess

dataset_name = "khlaifiabilel/military-aircraft-recognition-dataset"  # e.g., "username/dataset-name"
subprocess.run(["kaggle", "datasets", "download", "-d", dataset_name])