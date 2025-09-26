import numpy as np 
import pandas as pd 
import argparse 

#Creación de un objeto de conexión
parser = argparse.ArgumentParser(description='Programa en Python para graficar histograma dados sus parámetros') #Igual siempre
parser.add_argument('media', help= 'Valor promedio del histograma') #Sólo cambia el argumento que se quiere recibir
parser.add_argument('desv', help='Error estándar del histograma') #Sólo cambia el argumento que se quiere recibir
parser.add_argument('--n', default=100, help='Tamaño de la muestra')
args = parser.parse_args() #Igual siempre


n = int(args.n)  
media = float(args.media) 
desv = float(args.desv)

datos = np.random.normal(size = n, loc = media, scale = desv) 
datos = datos.round(0).astype(int) 

datos_trim = [] 
for i in range(len(datos)): 
  if datos[i] <= abs(media) + 2*desv or datos[i] >= abs(media) - 2*desv: 
    datos_trim.append(datos[i]) 

datos_trim = pd.DataFrame(datos_trim) 
datos_trim.columns = ['Datos'] 
histograma = datos_trim.groupby('Datos').size() 

for i in range(len(histograma)): 
  if histograma.index[i]>=0: 
    s = "+" 
  else: 
    s = "" 
  print( 
    s, 
    histograma.index[i], 
    ' '*(1+len(str(np.max([np.max(histograma.index), 
                           abs(np.min(histograma.index))]))) - 
                           len(str(abs(histograma.index[i])))), 
    '*'*round(100*histograma.iloc[i]/len(datos_trim)), 
    sep = "" 
    )
  
  