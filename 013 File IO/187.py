from pathlib import Path
import os
from translate import Translator

FILE_PATH = os.path.dirname(os.path.realpath(__file__)) + '\sample.txt'
OUPUT_FILE_PATH = os.path.dirname(
    os.path.realpath(__file__)) + '\\translated_sample.txt'
translator = Translator(to_lang='ja')

try:
    with open(FILE_PATH, mode='r') as my_file:
        print("READ FROM THE FILE...")
        input = my_file.read()
        print(input)
        print('TRANSLATED BELOW...')
        translated_input = translator.translate(input)
        print(translated_input)

        with open(OUPUT_FILE_PATH, mode='w', encoding="utf-8") as output_file:
            output_file.write(translated_input)


except FileNotFoundError as err:
    print('FILE DOES NOT EXIST')
    raise err

except IOError as err:
    raise err
