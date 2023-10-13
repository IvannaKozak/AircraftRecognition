# AircraftRecognition

## Instructions to Setting Up Data

### Using DVC (Recommended)
1. Ensure DVC is installed. If not, install using `pip install dvc`.
2. Run `DVC_data_setup.py` to set up the data.

### Manual Data Setup (Alternative)
1. Download your Kaggle API token from your Kaggle account page.
2. Save the `kaggle.json` file in the root directory.
3. Open folder `manual_setup`
3. Run `download_data.py` to download the dataset.
4. Run `unzip_data.py` to unzip the dataset.


# Documenting my work:

## Step 1
1) I created a script to download the dataset manually from Kaggle
2) Installed DVC and pushed my dataset to my Google Drive
3) Added my dataset folder to .gitignore (so that the dataset won't be pushed to GitHub)
4) Added kaggle.json and military-aircraft-recognition-dataset.zip to .gitignore

## Step 2
1) I made some data structure analyses to see what data I am working with
2) Saw that the test set is much bigger than the training set
3) Decided to split the data so that 80% of it will be the training set and 20% the test set
4) Saved the new split in the preparing_data folder, so that these files will be pushed to GitHub (and be the same for all people who try to run my code, no matter if they do a manual setup of data or use DVC)
5) Run the verify_imagesets.py to make sure my new train and test sets aren't overlapping
6) Run analyze_horizontal_boxes.py to see some examples of image annotation
7) Run analyze_oriented_boxes.py to see other examples of image annotation

## Step 3
The primary objective of this project is to develop a model for the recognition of military aircraft using annotated images. The Military Aircraft Recognition dataset will be used for this purpose. This dataset contains images of various military aircraft, annotated with both horizontal and oriented bounding boxes.

#### Task Definition:
The task is a multi-class classification problem where the goal is to correctly identify and classify different types of military aircraft (e.g., A1, A2, A10, etc.) from images. Furthermore, by utilizing the provided annotations, the project also encompasses an object detection component where the specific location of the aircraft in the image will be pinpointed.

#### Solution Strategy:
...
