import os
from PIL import Image

def resize_images_in_folder(folder_path, new_size):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                file_path = os.path.join(root, filename)
                with Image.open(file_path) as img:
                    img = img.resize(new_size, Image.LANCZOS)
                    img.save(file_path)

if __name__ == "__main__":
    folder_path = 'C:\Users\dawso\Downloads\ezgif-split'
    new_size = (80,80)  # Example size, change as needed
    resize_images_in_folder(folder_path, new_size)