import os
import xml.etree.ElementTree as ET

# Paths
ANNOTATIONS_PATH = "dataset/Annotations/Oriented Bounding Boxes/"
IMAGES_PATH = "dataset/JPEGImages/"
TRAIN_SET = "dataset/ImageSets/Main/train.txt"
TEST_SET = "dataset/ImageSets/Main/test.txt"

# Load train and test sets
with open(TRAIN_SET, 'r') as f:
    train_images = [line.strip() for line in f.readlines()]

with open(TEST_SET, 'r') as f:
    test_images = [line.strip() for line in f.readlines()]

# Analyze dataset structure
total_images = len(os.listdir(IMAGES_PATH))
total_objects = 0

for xml_file in os.listdir(ANNOTATIONS_PATH):
    tree = ET.parse(os.path.join(ANNOTATIONS_PATH, xml_file))
    root = tree.getroot()
    
    # Count the number of object elements in the XML
    total_objects += len(root.findall("object"))


print(f"Total Images: {total_images}")
print(f"Total Annotated Objects: {total_objects}")
print(f"Average Objects per Image: {total_objects/total_images:.2f}")


# Training and Test sets distribution
print(f"Number of Training Images: {len(train_images)}")
print(f"Number of Test Images: {len(test_images)}")

# Types distribution
types_count = {}

for xml_file in os.listdir(ANNOTATIONS_PATH):
    tree = ET.parse(os.path.join(ANNOTATIONS_PATH, xml_file))
    root = tree.getroot()
    
    for obj in root.findall("object"):
        obj_type = obj.find("name").text
        types_count[obj_type] = types_count.get(obj_type, 0) + 1

print("\nTypes Distribution:")
for obj_type, count in types_count.items():
    print(f"{obj_type}: {count}")

