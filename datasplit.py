import os
import shutil
import random

def split_data(source, dest_root, train_ratio=0.8, test_ratio=0.1):
    for label in os.listdir(source):
        label_path = os.path.join(source, label)
        if os.path.isdir(label_path):
            images = os.listdir(label_path)
            random.shuffle(images)

            total_size = len(images)
            train_size = int(total_size * train_ratio)
            test_size = int(total_size * test_ratio)

            train_images = images[:train_size]
            test_images = images[train_size:train_size + test_size]
            valid_images = images[train_size + test_size:]

            # Create train, test, and valid directories if not exist
            train_label_dir = os.path.join(dest_root, 'train', label)
            test_label_dir = os.path.join(dest_root, 'test', label)
            valid_label_dir = os.path.join(dest_root, 'valid', label)
            
            os.makedirs(train_label_dir, exist_ok=True)
            os.makedirs(test_label_dir, exist_ok=True)
            os.makedirs(valid_label_dir, exist_ok=True)

            # Move images to train directory
            for image in train_images:
                src_path = os.path.join(label_path, image)
                dest_path = os.path.join(train_label_dir, image)
                shutil.copy(src_path, dest_path)

            # Move images to test directory
            for image in test_images:
                src_path = os.path.join(label_path, image)
                dest_path = os.path.join(test_label_dir, image)
                shutil.copy(src_path, dest_path)

            # Move images to valid directory
            for image in valid_images:
                src_path = os.path.join(label_path, image)
                dest_path = os.path.join(valid_label_dir, image)
                shutil.copy(src_path, dest_path)

# Replace these paths with your actual paths
source_directory = '/workspace/YOLO_dataset_maker/videos/cloudkarya'
destination_directory = '/workspace/YOLO_dataset_maker/dataset'

# Create the destination root directory
os.makedirs(destination_directory, exist_ok=True)

# Split the data into train, test, and valid within the destination root
split_data(source_directory, destination_directory)
