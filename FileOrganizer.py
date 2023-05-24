import os
import shutil

# Define the source directory (your desktop)
source_directory = os.path.expanduser("~/Desktop")

# Define the destination directories for each file type
destination_directories = {
    "Images": os.path.expanduser("~/Desktop/Images"),
    "Documents": os.path.expanduser("~/Desktop/Documents"),
    "Videos": os.path.expanduser("~/Desktop/Videos"),
    "Others": os.path.expanduser("~/Desktop/Others")
}

# Create destination directories if they don't exist
for directory in destination_directories.values():
    if not os.path.exists(directory):
        os.makedirs(directory)

# Iterate over files in the source directory
for filename in os.listdir(source_directory):
    file_path = os.path.join(source_directory, filename)

    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Get the file extension
    _, extension = os.path.splitext(filename)

    # Determine the destination directory based on the file extension
    if extension.lower() in (".jpg", ".jpeg", ".png", ".gif"):
        destination = destination_directories["Images"]
    elif extension.lower() in (".doc", ".docx", ".txt", ".pdf"):
        destination = destination_directories["Documents"]
    elif extension.lower() in (".mp4", ".avi", ".mov"):
        destination = destination_directories["Videos"]
    else:
        destination = destination_directories["Others"]

    # Move the file to the appropriate destination directory
    shutil.move(file_path, os.path.join(destination, filename))

print("File organization complete!")
