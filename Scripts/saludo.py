#Ejercicio 2:
# Cree un programa en python llamado saludo.py en la carpeta Scripts que reciba como argumento opcional el texto Hola 
# y devuelva como respuesta una de las siguientes posibilidades:
# Hola, cómo estas? con una probabilidad del 50%
# Hola, me llamo Computina con una probabilidad del 25%
# Háblale a la mano con una probabilidad del 25%
# Si recibe algo distinto a Hola la respuesta debería ser Saluda, primero!!!.

import random
import argparse 
parser= argparse.ArgumentParser(description = "Programa de saludar")
parser.add_argument('--saludo', default= 'saluda primero')
args= parser.parse_args()
mensaje= str(args.saludo)              
dr= random.randint(1,100)
try:
    if mensaje == 'Hola':
        if dr <= 50:
            print('Hola, cómo estas?')
        elif dr <= 75:
            print('Hola, me llamo Computina')
        else:
            print('Háblale a la mano')
    else:
        print('Saluda primero')               
except:
    print('algo hiciste mal')