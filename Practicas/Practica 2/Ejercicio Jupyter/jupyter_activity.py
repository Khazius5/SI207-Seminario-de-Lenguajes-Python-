#. Dado el siguiente texto guardado en la varible jupyter_info, solicite por teclado una letra e imprima
#   las palabras que comienzan con dicha letra. En caso que no se haya inrgesado un letra, indique el
#   error. Ver: módulo string

from jupyter_info import JUPYTER_INFO as jupyter_text
import string


def start():
    """La función start ejecuta el programa"""
    letter = input("Ingrese una letra: ")
    if (letter in string.ascii_letters):
        print(f'Las palabras que comienzan con la letra {letter} son: ')
        for word in jupyter_text.split():
            if (word[0] == letter):
                print(word)
    else:
        print("Error, no se ingreso una letra")


start()