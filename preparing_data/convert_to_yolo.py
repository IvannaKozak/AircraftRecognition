import os
import xml.etree.ElementTree as ET

class_map = {
    'A2': 0,
    'A10': 1,
    'A3': 2,
    'A19': 3,
    'A1': 4,
    'A13': 5,
    'A20': 6,
    'A15': 7,
    'A16': 8,
    'A17': 9,
    'A12': 10,
    'A5': 11,
    'A14': 12,
    'A7': 13,
    'A9': 14,
    'A4': 15,
    'A18': 16,
    'A8': 17,
    'A11': 18,
    'A6': 19
}

def convert_annotation(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    print("Started converton")

    for xml_file in os.listdir(input_folder):
        if xml_file.endswith('.xml'):
            tree = ET.parse(os.path.join(input_folder, xml_file))
            root = tree.getroot()
            
            # Fetch the width and height of the image
            width = int(root.find('size/width').text)
            height = int(root.find('size/height').text)

            if width == 0 or height == 0:
                print(f"Error: XML file {xml_file} has a width or height of zero!")
                continue
            
            out_path = os.path.join(output_folder, xml_file.replace('.xml', '.txt'))
            
            with open(out_path, 'w') as f:
                for obj in root.iter('object'):

                    xmlbox = obj.find('bndbox')

                    if xmlbox is None:
                        print(f"Error: XML file {xml_file} does not have a bndbox for one of its objects!")
                        continue

                    cls = obj.find('name').text
                    cls_id = class_map.get(cls)
                    if cls_id is None:
                        raise ValueError(f"Class {cls} not found in class_map!")
                    
                    # Fetch the bounding box coordinates
                    
                    b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text),
                         float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
                    yolo_format = convert_to_yolo_format(b, width, height)
                    f.write(f"{cls_id} {' '.join([str(a) for a in yolo_format])}\n")


def convert_to_yolo_format(box, img_width, img_height):
    """
    Convert the bounding box in XML format (xmin, xmax, ymin, ymax) 
    to YOLO format (x_center, y_center, width, height), normalized to [0,1].
    """
    dw = 1./img_width
    dh = 1./img_height
    x_center = (box[1] + box[0])/2.0
    y_center = (box[3] + box[2])/2.0
    width = box[1] - box[0]
    height = box[3] - box[2]
    
    x_center *= dw
    width *= dw
    y_center *= dh
    height *= dh

    return (x_center, y_center, width, height)


if __name__ == '__main__':
    # Modify these paths accordingly
    horz_input_folder = 'dataset/Annotations/Horizontal Bounding Boxes'
    horz_output_folder = 'dataset/JPEGImages'

    convert_annotation(horz_input_folder, horz_output_folder)
    print("Finished horizontal bounding boxes")
