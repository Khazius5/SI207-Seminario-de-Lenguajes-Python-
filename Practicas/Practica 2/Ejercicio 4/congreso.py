#Para la aceptación de un artículo en un congreso se definen las siguientes especificaciones que
#   deben cumplir y recomendaciones de escritura:
#           • título: 10 palabras como máximo
#           • cada oración del resumen:
#                 ▪ hasta 12 palabras: fácil de leer
#                 ▪ entre 13-17 palabras: aceptable para leer
#                 ▪ entre 18-25 palabras: difícil de leer
#                 ▪ mas de 25 palabras: muy difícil
#Dado un artículo en formato string, defina si cumple las especificaciones del título y cuántas oraciones
#tiene de cada categoría. El formato estándar en que recibe el string tiene la siguiente forma:
# En este ejemplo se debe informar:
#   • título: ok
#   • Cantidad de oraciones fáciles de leer: 1, aceptables para leer: 2, dificil de leer: 1, muy difícil de leer: 2

from evaluar import ARTICLE as art

def count_title():
    """La funcion retorna Ok si el titulo contiene menos de 10 palabras, sino, un warning de que el titulo sobrepasa las palabras permitidas"""
    article = art.split("resumen:")
    title = article[0].split(" ")[2:]
    if (len(title) <= 10):
        print("Titulo: Ok")
    else:
        print("El titulo sobrepasa las palabras permitidas")

def count_overview():
    """La funcion overview retorna la cantidad de parrafos faciles, aceptables, dificiles o muy dificiles de leer"""
    article = art.split("resumen:")
    overview = article[1].split(".")
    easy = 0
    acceptable = 0
    difficult = 0
    very_difficult = 0
    for words in overview:
        ph = words.split(".")
        x = ph[0].split()
        if len(x) <= 12:
            easy += 1
        elif len(x) <= 17:
            acceptable += 1
        elif len(x) <= 25:
            difficult += 1
        else:
            very_difficult += 1
    print(f'Cantidad de oraciones fáciles de leer: {easy}, aceptables para leer: {acceptable}, dificil de leer: {difficult}, muy difícil de leer: {very_difficult}')


def start():
    """Ejecuta el programa"""
    count_title()
    count_overview()
   
start()

