import os
from PIL import Image, ImageFilter

dir_path = os.path.dirname(os.path.realpath(__file__))
file_path = dir_path+'/pokedex/pikachu.jpg'
result_path = dir_path+'/pokedex_result/pikachu.png'

img = Image.open(file_path)

# Filtered_Img = img.filter(ImageFilter.BLUR)
Filtered_Img = img.convert('L')
Filtered_Img = Filtered_Img.rotate(90)

Filtered_Img.save(result_path, 'png')
Filtered_Img.show()
