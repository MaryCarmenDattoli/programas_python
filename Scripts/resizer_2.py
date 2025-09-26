# resizer_2.py

from PIL import Image
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('input_file', help='ruta del archivo de entrada')
parser.add_argument('output_file', help='ruta del archivo de salida')
parser.add_argument('new_size', help='tamaño de imagen', type=tuple)
args = parser.parse_args()

try:
    im = Image.open(args.input_file)

except Exception as error_msg:
    print(error_msg)
    print('the default image is used')
    im = Image.open('default_input.png')

resized = im.resize(args.new_size)
resized.save(args.output_file)
im.close()