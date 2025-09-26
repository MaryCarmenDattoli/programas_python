# Ejercicio 1: 
# Dentro de la carpeta Scripts cree un programa llamado res_estadistico.py que reciba como input desde la consola 
# un archivo csv con un solo conjunto de datos, y retorne como resultado un resumen estadístico que incluya 
# los siguientes indicadores:
# 1. Tamaño de la muestra
# 2. Media
# 3. Mediana
# 4. Cuartil 1
# 5. Cuartil 2
# 6. Rango Interquartil
# Para probar que su script funciona puede probar con el siguiente conjunto de datos: https://raw.githubusercontent.com/jsaraujott/datos/main/datos.csv

# importa las librerías necesarias
import numpy as np 
import pandas as pd 
import argparse
#Creae un objeto de coneccion
parser = argparse.ArgumentParser(description= "Resumen estadistico")
parser.add_argument("input",help="archivo csv")
args = parser.parse_args() 
df= pd.read_csv(args.input)
print(df.describe())