from PIL import Image, ImageEnhance, ImageFilter
import os

# store images you'd like to edit inside imgs folder
path = './imgs'
# all edited images will be stored in editedImgs
pathOut = '/editedImgs'

# for each images in imgs directory, it will apply the same effects
for filename in os.listdir(path):
    img = Image.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN).convert("L").rotate(-90)
    factor = 1.5
    enhancer = ImageEnhance.Contrast(edit)
    edit = enhancer.enhance(factor)
    clean_name = os.path.splitext(filename)[0]

    edit.save(f".{pathOut}/{clean_name}_edited.jpg")

# Python Image Editing Library Pillow - https://pillow.readthedocs.io/en/stable/
