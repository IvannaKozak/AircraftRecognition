import zipfile

with zipfile.ZipFile('military-aircraft-recognition-dataset.zip', 'r') as zip_ref:
    zip_ref.extractall('dataset')