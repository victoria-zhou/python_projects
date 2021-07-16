import sys
import os
from PIL import Image, ImageFilter

img_folder = sys.argv[1]
output_folder = sys.argv[2]

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(img_folder):
    img = Image.open(f'{img_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    print(clean_name)
    img.save(f'{output_folder}{clean_name}.png', 'png')
    print('all done')
#
# for each in first:
#     each = Image.convert(each, 'png')
#     each.save()

print(img_folder, output_folder)
