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


def start():
    """La función start ejecuta el programa"""
    article = art.split('\n')
    title = article[0].split(' ')[1:]
    if len(title) > 10:
        print('El título tiene más de 10 palabras')
    else:
        print('título: ok')
    easy = 0
    acceptable = 0
    difficult = 0
    very_difficult = 0
    for sentence in article[1:]:
        words = sentence.split(' ')
        if len(words) <= 12:
            easy += 1
        elif len(words) <= 17:
            acceptable += 1
        elif len(words) <= 25:
            difficult += 1
        else:
            very_difficult += 1
    print(f'Cantidad de oraciones fáciles de leer: {easy}, aceptables para leer: {acceptable}, dificil de leer: {difficult}, muy difícil de leer: {very_difficult}')


start()