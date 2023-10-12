with open("dataset/ImageSets/Main/train.txt", "r") as f:
    train_images = set(f.readlines())

with open("dataset/ImageSets/Main/test.txt", "r") as f:
    test_images = set(f.readlines())

overlap = train_images.intersection(test_images)
if overlap:
    print("Overlapping images:", overlap)
else:
    print("No overlap between train and test images.")
