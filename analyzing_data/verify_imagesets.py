with open("preparing_data/new_train.txt", "r") as f:
    train_images = set(f.readlines())

with open("preparing_data/new_test.txt", "r") as f:
    test_images = set(f.readlines())

overlap = train_images.intersection(test_images)
if overlap:
    print("Overlapping images:", overlap)
else:
    print("No overlap between train and test images.")
