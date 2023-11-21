import os
import shutil

DIRECTORIES = ['C:/Users/Okami/Downloads', 'E:/Downloads']
DESTINATIONS = ['C:/Users/Okami/Downloads', 'E:/Downloads']


def organize_directory(source_dir, destination_dir):
    # Create the destination directory if it doesn't exist
    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    # Iterate through each file in the source directory
    for filename in os.listdir(source_dir):
        source_path = os.path.join(source_dir, filename)

        # Skip directories
        if os.path.isdir(source_path):
            continue

        # Get the file extension
        _, file_extension = os.path.splitext(filename)

        # Create a directory for the file type if it doesn't exist
        file_type_dir = os.path.join(destination_dir, file_extension[1:].lower())  # Remove the leading dot
        if not os.path.exists(file_type_dir):
            os.makedirs(file_type_dir)

        # Move the file to the corresponding directory
        destination_path = os.path.join(file_type_dir, filename)
        shutil.move(source_path, destination_path)


if __name__ == "__main__":
    # Specify the source and destination directories
    for n in range(len(DIRECTORIES)):
        source_directory = DIRECTORIES[n - 1]
        destination_directory = DESTINATIONS[n - 1]

        # Organize the directory
        organize_directory(source_directory, destination_directory)

        print(f"Files organized in {destination_directory}")
