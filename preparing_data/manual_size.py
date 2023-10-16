import os
from PIL import Image
import xml.etree.ElementTree as ET


xml_directory = 'dataset/Annotations/Horizontal Bounding Boxes'
image_directory = 'dataset/JPEGImages'

# List of problematic XML files
error_files = [
    '326.xml',
    '334.xml',
    '335.xml',
    '338.xml',
    '340.xml',
    '348.xml',
    '349.xml',
    '405.xml',
    '409.xml',
    '420.xml',
    '421.xml',
    '426.xml',
    '429.xml',
    '430.xml',
    '431.xml',
    '442.xml',
    '443.xml',
    '452.xml',
    '476.xml',
    '480.xml',
    '482.xml',
]

for xml_file in error_files:
    # Construct the full paths for XML and its associated image
    xml_path = os.path.join(xml_directory, xml_file)
    image_name = xml_file.replace('.xml', '.jpg')  # Assuming images are in .jpg format
    image_path = os.path.join(image_directory, image_name)

    # Open the image using PIL and get its dimensions
    image = Image.open(image_path)
    width, height = image.size

    # Parse the XML
    tree = ET.parse(xml_path)
    root = tree.getroot()

    # Find the <width> and <height> tags and update their text
    width_tag = root.find('.//size/width')
    height_tag = root.find('.//size/height')
    if width_tag is not None:
        width_tag.text = str(width)
    if height_tag is not None:
        height_tag.text = str(height)

    # Save the modified XML
    tree.write(xml_path)

print("Bad XML files updated successfully!")
