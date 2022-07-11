# JPG to PNG Convertor
# Run Instructions: Terminal command: "d:/Python Training/017 Scripting with Python/212.py" '\pokedex' '\pokedex_result'

import os
import sys
from PIL import Image
from pathlib import Path

dir_path = os.path.dirname(os.path.realpath(__file__))
# SOURCE_FOLDER = dir_path + '/pokedex'
SOURCE_FOLDER = dir_path + sys.argv[1]
# DESTINATION_FOLDER = dir_path + '/pokedex_result'
DESTINATION_FOLDER = dir_path + sys.argv[2]
os.makedirs(DESTINATION_FOLDER, exist_ok=True)

# Get the all the Pokedex images
pokedex_list = []
# Iterate directory
for path in os.listdir(SOURCE_FOLDER):
    # check if current path is a file
    if os.path.isfile(os.path.join(SOURCE_FOLDER, path)) and path.endswith('.jpg'):
        pokedex_list.append(os.path.join(SOURCE_FOLDER, path))

# Convert the jpg images to png images
for i in pokedex_list:
    with Image.open(i) as img:
        file_name = Path(i).stem
        img.save(DESTINATION_FOLDER+'/'+file_name+'.png', 'png')
