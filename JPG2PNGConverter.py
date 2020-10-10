import sys
import os
from PIL import Image

# grab first and second argument from commandline
print('This is the name of script: ', sys.argv[0])
print('Number of arguments: ', len(sys.argv))
print('The arguments are: ', str(sys.argv))

images_folder = sys.argv[1]
converted_images_folder = sys.argv[2]

# check if folders from commandline arguments exists
print('Check folders from command line arguments: ', sys.argv[1], os.path.exists(images_folder), sys.argv[2], os.path.exists(converted_images_folder) )

if not os.path.exists(images_folder):
    print('Image Folder in first Argument does not exist - noting to convert - exit', images_folder)
    raise SystemExit

if not os.path.exists(converted_images_folder):
    print('Image Folder for converted Images in second Argument does not exist: ', converted_images_folder)
    print('Creating it')
    os.makedirs(converted_images_folder)
    print('Check folders again: ', sys.argv[1], os.path.exists(images_folder), sys.argv[2],
          os.path.exists(converted_images_folder))

# loop through image folder
# convert images to png
# save images to new folder

for file in os.listdir(images_folder):
    filename = os.fsdecode(file)
    if filename.endswith(".jpg"):
        clean_name = os.path.splitext(os.path.join(converted_images_folder, filename))[0]+'.png'
        if not os.path.exists(clean_name):
            print('Found image: ', os.path.join(images_folder, filename))
            img = Image.open(os.path.join(images_folder, filename))
            img.save(clean_name, 'png')
            print('Converted to: ', clean_name)
        else:
            print('File already converted - skipped: ', clean_name)
        continue
    else:
        continue
