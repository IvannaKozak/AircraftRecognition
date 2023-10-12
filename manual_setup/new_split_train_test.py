import random


TRAIN_SET = "dataset/ImageSets/Main/train.txt"
TEST_SET = "dataset/ImageSets/Main/test.txt"

# Load train and test sets
with open(TRAIN_SET, 'r') as f:
    train_images = [line.strip() for line in f.readlines()]

with open(TEST_SET, 'r') as f:
    test_images = [line.strip() for line in f.readlines()]

# Combine current train and test sets
all_images = train_images + test_images

# Shuffle the combined list
random.shuffle(all_images)

# Split into training and test sets (using an 80-20 split as an example)
split_index = int(0.8 * len(all_images))
new_train_images = all_images[:split_index]
new_test_images = all_images[split_index:]

print(f"Number of New Training Images: {len(new_train_images)}")
print(f"Number of New Test Images: {len(new_test_images)}")

# Paths for new split files
NEW_TRAIN_SET = "dataset/ImageSets/new_train.txt"
NEW_TEST_SET = "dataset/ImageSets/new_test.txt"

# Write the new split to new_train.txt and new_test.txt
with open(NEW_TRAIN_SET, 'w') as f:
    for img in new_train_images:
        f.write(f"{img}\n")

with open(NEW_TEST_SET, 'w') as f:
    for img in new_test_images:
        f.write(f"{img}\n")

print("Created new_train.txt and new_test.txt with the new split.")


