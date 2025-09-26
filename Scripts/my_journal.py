from datetime import datetime

# obtiene la hora actual
now = datetime.now() 

with open('my_journal.txt', 'a') as f:
    f.write('\n')     # comienza con una nueva línea
    f.write(str(now)) # marca temporal
    f.write('\n\n')   # inserta una línea en blanco
    f.write(' ')      # espacio vacío
    f.write(input())  # escribe una entrada en el diario desde el teclado
    f.write('\n\n')   # termina con una línea en blanco