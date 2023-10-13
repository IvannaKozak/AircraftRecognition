from sklearn.model_selection import train_test_split

TRAIN_SET = "dataset/ImageSets/Main/train.txt"
TEST_SET = "dataset/ImageSets/Main/test.txt"

# Load train and test sets
with open(TRAIN_SET, 'r') as f:
    train_images = [line.strip() for line in f.readlines()]

with open(TEST_SET, 'r') as f:
    test_images = [line.strip() for line in f.readlines()]

# Combine current train and test sets
all_images = train_images + test_images

# Split into training and test sets using scikit-learn (80-20 split)
new_train_images, new_test_images = train_test_split(all_images, test_size=0.2, random_state=42)

print(f"Number of New Training Images: {len(new_train_images)}")
print(f"Number of New Test Images: {len(new_test_images)}")

# Paths for new split files
NEW_TRAIN_SET = "new_train.txt"
NEW_TEST_SET = "new_test.txt"

# Write the new split to new_train.txt and new_test.txt
with open(NEW_TRAIN_SET, 'w') as f:
    for img in new_train_images:
        f.write(f"{img}\n")

with open(NEW_TEST_SET, 'w') as f:
    for img in new_test_images:
        f.write(f"{img}\n")

print("Created new_train.txt and new_test.txt with the new split using scikit-learn.")
