import os
from PIL import Image

# Define the source and target file extensions
source_extension = ".jpg"
target_extension = ".png"

# Get the current directory
current_directory = os.getcwd()

# Iterate over files in the current directory
for filename in os.listdir(current_directory):
    if filename.endswith(source_extension):
        # Construct the source and target file paths
        source_path = os.path.join(current_directory, filename)
        target_path = os.path.join(current_directory, filename.replace(source_extension, target_extension))

        # Open the source image
        try:
            image = Image.open(source_path)
        except Exception as e:
            print(f"Error opening {source_path}: {e}")
            continue

        # Save the image with the target extension
        try:
            image.save(target_path)
            print(f"Converted {source_path} to {target_path}")
        except Exception as e:
            print(f"Error saving {target_path}: {e}")

print("Conversion complete.")
