import os
from PIL import Image, UnidentifiedImageError

def crop_image(image_path, crop_width, crop_height):
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            left = (width - crop_width) // 2
            upper = (height - crop_height) // 2
            right = left + crop_width
            lower = upper + crop_height
            # Ensure crop area is within image bounds
            if left < 0 or upper < 0 or right > width or lower > height:
                print(f"Invalid crop area for image {image_path}")
                return
            cropped_img = img.crop((left, upper, right, lower))
            cropped_img.save(image_path)
    except UnidentifiedImageError:
        print(f"Cannot identify image file {image_path}")

def process_folder(folder_path, crop_width, crop_height):
    for root, _, files in os.walk(folder_path):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                image_path = os.path.join(root, file)
                crop_image(image_path, crop_width, crop_height)

if __name__ == "__main__":
    folder_path = 'D:\Python\Python23-24\Python23-24\Term2\pewpew\Assets\sprites\monster\WitchDoc'
    crop_width = 289  # Example crop width
    crop_height = 276  # Example crop height
    process_folder(folder_path, crop_width, crop_height)