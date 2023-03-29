#1. Tomando el texto del README.md de numpy, copiar y pegar el texto en una variable, luego
    #imprima todas las líneas que contienen 'http' o 'https'.
#2. Indique la palabra que aparece mayor cantidad de veces en el texto del README.md de numpy.
    #Copie y pegue el texto en una varible.

from README_numpy import README as numpy_text
from collections import Counter
import string


def finder():
    """La función finder realiza una busqueda iterada por un for buscando e imprimiendo
        las lineas que contengan http o https"""
    new_text = numpy_text.split('\n') #Dividimos el archivo README en los saltos de linea que contiene
    new_text = list(filter(lambda x: x.strip(), new_text)) #Quitamos los saltos de linea de la lista generada anteriormente
    for line in new_text:
        if ('http' in line):
                print(line)
                print("-"*15)

def max():
    """La funcion max extrae la palabra más comun del archivo README"""
    max_text = numpy_text.split() #Nuevamente dividimos el archivo pero esta vez en palabras
    max_text = list(filter(lambda x: x.strip(), max_text)) #Nuevamente quitamos los espacios en blanco
    count = Counter(max_text) 
    max_common = count.most_common()
    if (max_common[0][0] == string.ascii_letters):
        print(f'La palabra más comun en el README de Numpy es {max_common[0][0]} ')
    else:
        print((f'La palabra más comun en el README de Numpy es: {max_common[1][0]} con un total de: {max_common[1][1]}'))

def start():
    """Ejecuta el programa con todas sus funciones"""
    finder()
    max()

start()