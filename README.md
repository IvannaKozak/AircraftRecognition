# AircraftRecognition


## Setting Up Data

### Using DVC (Recommended)
1. Ensure DVC is installed. If not, install using `pip install dvc`.
2. Run `DVC_data_setup.py` to set up the data.

### Manual Data Setup (Alternative)
1. Download your Kaggle API token from your Kaggle account page.
2. Save the `kaggle.json` file in the root directory.
3. Open folder `manual_setup`
3. Run `download_data.py` to download the dataset.
4. Run `unzip_data.py` to unzip the dataset.