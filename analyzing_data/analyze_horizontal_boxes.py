import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import xml.etree.ElementTree as ET

img_path = "dataset/JPEGImages/3831.jpg"
img = Image.open(img_path)
fig, ax = plt.subplots(1)
ax.imshow(img)

tree = ET.parse("dataset/Annotations/Oriented Bounding Boxes/3831.xml")
root = tree.getroot()

for obj in root.findall("object"):
    bbox = obj.find("bndbox")
    xmin = int(bbox.find("xmin").text)
    ymin = int(bbox.find("ymin").text)
    xmax = int(bbox.find("xmax").text)
    ymax = int(bbox.find("ymax").text)
    rect = patches.Rectangle((xmin, ymin), xmax - xmin, ymax - ymin, linewidth=1, edgecolor="r", facecolor="none")
    ax.add_patch(rect)

plt.show()
