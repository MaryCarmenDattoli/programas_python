import json
import requests # librería para obtener datos de internet

# descargar (obtener) un archivo json de internet
data = requests.get('https://dummyjson.com/products/1')

# extraer el contenido del archivo json descargado
text = data.text

# análisis sintáctico del contenido mediante la función loads
print(json.loads(text))