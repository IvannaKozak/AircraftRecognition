# AircraftRecognition Test Task

## Instructions to Setting Up Data

### 1. Using DVC (Recommended)
1. Ensure DVC is installed. If not, install using `pip install dvc`.
2. Run `DVC_data_setup.py` to set up the data.

### 1. Manual Data Setup (Alternative)
1. Download your Kaggle API token from your Kaggle account page.
2. Save the `kaggle.json` file in the root directory.
3. Open folder `manual_setup`.
4. Run `download_data.py` to download the dataset.
5. Run `unzip_data.py` to unzip the dataset.

### 2. Preparing data
1. Open folder `preparing_data`.
2. Run `manual_size.py`.
3. Run `convert_to_yolo.py`.
4. Run `modifying_data.py`.

### 3. Training the model
1. Clone the YOLOv5 model: `git clone https://github.com/ultralytics/yolov5`.
2. Run `pip install -qr requirements.txt comet_ml`.
3. Run command `python train.py --img 640 --batch 16 --epochs 30 --data ../preparing_data/my_dataset.yaml --cfg yolov5s.yaml --weights yolov5s.pt --name my_model`.


# Documenting my work:

## Step 1
1) I created a script to download the dataset manually from Kaggle.
2) Installed DVC and pushed my dataset to my Google Drive.
3) Added my dataset folder to .gitignore (so that the dataset won't be pushed to GitHub).
4) Added kaggle.json and military-aircraft-recognition-dataset.zip to .gitignore.

## Step 2
1) I made some data structure analyses to see what data I am working with.
2) Saw that the test set is much bigger than the training set.
3) Decided to split the data so that 80% of it will be the training set and 20% the test set.
4) Saved the new split in the `preparing_data` folder, so that these files will be pushed to GitHub (and be the same for all people who try to run my code, no matter if they do a manual setup of data or use DVC).
5) I ran the `verify_imagesets.py` to make sure my new train and test sets aren't overlapping.
6) I ran `analyze_horizontal_boxes.py` to see some examples of image annotation.
7) I ran `analyze_oriented_boxes.py` to see other examples of image annotation.

## Step 3
The primary objective of this project is to develop a model for the recognition of military aircraft using annotated images. The Military Aircraft Recognition dataset will be used for this purpose. This dataset contains images of various military aircraft, annotated with both horizontal and oriented bounding boxes.

#### Task Definition:
The task is a multi-class classification problem where the goal is to correctly identify and classify different types of military aircraft (e.g., A1, A2, A10, etc.) from images. Furthermore, by utilizing the provided annotations, the project also encompasses an object detection component where the specific location of the aircraft in the image will be pinpointed.

#### Solution Strategy:
My solution strategy is to use pretrained model YOLOv5 and train it on my own data. I chose this model because it is famous for its fast speed, high accuracy, and easy installation and use. It's a modern object detection algorithm, that has been written in PyTorch.

## Step 4
I prepared the dataset to solve the task:
1. I ran `convert_to_yolo.py` and saw that some images don't have weight and height in their XML files.
2. So I ran `manual_size.py` to manually add this information to the XML files.
3. Then I ran `convert_to_yolo.py` again, and received .txt file for each image.
4. I ran `modifying_data.py` to create files with paths to each image like this: `../dataset/JPEGImages/403.jpg`
5. Then I created a file `my_dataset.yaml` with all the necessary information for the model.

## Step 5
I trained the model using this command:
`python train.py --img 640 --batch 3 --epochs 3 --data ../preparing_data/my_dataset.yaml --cfg yolov5s.yaml --weights yolov5s.pt --name my_model`
I used that little amount of epochs and batch, cause I run the training on my laptop, and it doesn't have enough RAM.
If more epochs and batches were set, the results would be much better.
Epochs should be set to at least 30 and batches = 16 or more.

The results of the training are in the folder `my_model`. They aren't good, but that's mainly because of the low amount of epochs and batches. Using more epochs(for example 30) would take more than 40 hours to complete.
Because of that poor accuracy, I didn't run the validation, cause it wouldn't make any sense.

One way to solve this problem with a time and RAM-consuming training process would be to use a cloud-based solution with GPUs, like Google Colab. Also, there is a possibility to run the training directly on Kaggle. But I wanted to do it locally on my computer, to be able to do each step separately and be able to commit and push everything to GitHub.