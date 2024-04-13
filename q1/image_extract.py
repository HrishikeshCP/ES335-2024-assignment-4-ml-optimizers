import os
from bing_image_downloader import downloader
from PIL import Image

# Function to download images
def download_images(keyword, output_dir, limit=100):
    images = downloader.download(keyword, limit=limit, output_dir=output_dir, adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
    return images

# Function to convert non-jpg images to jpg format
def convert_to_jpg(images, keyword, output_dir):
    for img in images:
        img_path = os.path.join(output_dir, keyword, img['filename'])
        img_extension = os.path.splitext(img_path)[-1].lower()
        if img_extension != '.jpg':
            # Convert image to jpg format
            with Image.open(img_path) as image:
                image = image.convert('RGB')
                jpg_path = os.path.splitext(img_path)[0] + '.jpg'
                image.save(jpg_path)
            os.remove(img_path)
            img['filename'] = os.path.basename(jpg_path)
            img['path'] = jpg_path
        else:
            img['path'] = img_path

# Download images for 'Monkey'
# monkey_images = download_images('Monkey', output_dir='dataset')
# 
# Download images for 'Rabbit'
# rabbit_images = download_images('Rabbit', output_dir='dataset')
# 
# Convert non-jpg images to jpg format
# convert_to_jpg(monkey_images, 'Monkey', 'dataset')
# convert_to_jpg(rabbit_images, 'Rabbit', 'dataset')

# Create dataset folder with two classes and corresponding labels

monkey_images = []
rabbit_images = []

monkey_dir = 'dataset/Monkey'
rabbit_dir = 'dataset/Rabbit'

# Load monkey images
for filename in os.listdir(monkey_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        img = Image.open(os.path.join(monkey_dir, filename))
        monkey_images.append(img)

# Load rabbit images
for filename in os.listdir(rabbit_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        img = Image.open(os.path.join(rabbit_dir, filename))
        rabbit_images.append(img)




dataset_dir = 'dataset'
classes = ['Monkey', 'Rabbit']
for cls in classes:
    cls_dir = os.path.join(dataset_dir, cls)
    if not os.path.exists(cls_dir):
        os.makedirs(cls_dir)
# Move downloaded images to corresponding class folders
for img in monkey_images:
    # src = img['path']
    dst = os.path.join(dataset_dir, 'Monkey', img)
    os.rename(img, dst)

for img in rabbit_images:
    src = img['path']
    dst = os.path.join(dataset_dir, 'Rabbit', img['filename'])
    os.rename(src, dst)

# Generate labels file
with open(os.path.join(dataset_dir, 'labels.txt'), 'w') as f:
    for img in monkey_images:
        f.write(f"{img['filename']} Monkey\n")
    for img in rabbit_images:
        f.write(f"{img['filename']} Rabbit\n")

print("Dataset creation completed.")
