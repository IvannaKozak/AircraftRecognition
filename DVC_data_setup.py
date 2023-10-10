import os
import subprocess

def data_exists(data_directory):
    """
    This function checks if the dataset exists in the given directory.
    For simplicity, it checks the directory's existence.
    """
    return os.path.exists(data_directory)

def main():
    dataset_directory = "dataset"

    if not data_exists(dataset_directory):
        print("Dataset not found. Fetching using DVC...")
        subprocess.run(["dvc", "pull"])
        print("Dataset fetched successfully!")
    else:
        print("Dataset already exists.")

if __name__ == "__main__":
    main()
