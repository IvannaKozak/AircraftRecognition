import matplotlib.pyplot as plt
import matplotlib.patches as patches
from PIL import Image
import xml.etree.ElementTree as ET

# Load image
img_path = "dataset/JPEGImages/3831.jpg"
img = Image.open(img_path)
fig, ax = plt.subplots(1)
ax.imshow(img)

# Load corresponding annotation for Oriented Bounding Boxes
tree = ET.parse("dataset/Annotations/Oriented Bounding Boxes/3831.xml")
root = tree.getroot()

for obj in root.findall("object"):
    robndbox = obj.find("robndbox")
    
    x_lt = float(robndbox.find("x_left_top").text)
    y_lt = float(robndbox.find("y_left_top").text)
    
    x_rt = float(robndbox.find("x_right_top").text)
    y_rt = float(robndbox.find("y_right_top").text)
    
    x_rb = float(robndbox.find("x_right_bottom").text)
    y_rb = float(robndbox.find("y_right_bottom").text)
    
    x_lb = float(robndbox.find("x_left_bottom").text)
    y_lb = float(robndbox.find("y_left_bottom").text)
    
    polygon = patches.Polygon([(x_lt, y_lt), (x_rt, y_rt), (x_rb, y_rb), (x_lb, y_lb)], closed=True, edgecolor='r', facecolor='none')
    ax.add_patch(polygon)

plt.show()
