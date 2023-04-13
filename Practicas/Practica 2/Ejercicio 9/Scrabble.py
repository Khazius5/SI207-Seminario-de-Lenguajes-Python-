#Escriba un programa que solicite por teclado una palabra y calcule el valor de la misma dada la
#siguiente tabla de valores del juego Scrabble:

from values import SCRABBLE_VALUES

def main():
    """Pide al usuario que ingrese una palabra y calcula el valor de la misma"""
    word = input("Ingrese una palabra: ").upper()
    valor = 0
    for char in word:
        valor += SCRABBLE_VALUES[char]
    print(f"El valor de la palabra {word} es de {valor}")

if __name__ == "__main__":
    main()

