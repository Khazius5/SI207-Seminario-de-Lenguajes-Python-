import os

PATH = os.path.dirname(os.path.abspath(__file__)) # Obtener la ubicación del archivo
os.chdir(PATH) # Cambiar el directorio de trabajo a la ubicación del archivo

def encripto(cadena, invertida=True):
    """Guarda la palabra cifrada en un archivo de texto"""
    with open("texto.txt", "a") as archivo:
        # Escribir cadena cifrada en el archivo
        cadena_encriptada = list(map(lambda x: chr(ord(x) + 1), cadena))
        cadena_encriptada = "".join(cadena_encriptada)
        cadena_cifrada = cadena_encriptada[::-1] if invertida else cadena_encriptada
        archivo.write(cadena_cifrada + "\n")

def guardar_original(cadena_original):
    """Guarda la palabra original en un archivo de texto"""
    with open("texto_original.txt", "a") as archivo:
        archivo.write(cadena_original + "\n")


def mostrar_resultados():
    """Muestra las palabras cifradas y las palabras originales en una tabla de 3 columnas"""
    with open("texto.txt", "r") as archivo:
        lista_cifrada = archivo.readlines()
    with open("texto_original.txt", "r") as archivo:
        lista_original = archivo.readlines()
    print("--------------------------------------------------------------------------")
    print("Palabra original     Palabra cifrada normal     Palabra cifrada invertida")
    print("--------------------------------------------------------------------------")
    for i in range(len(lista_original)):
        print(f"{lista_original[i].strip():<20}{lista_cifrada[i].strip():<25}{lista_cifrada[i].strip()[::-1]:<25}")


def main():
    """Pide al usuario que ingrese palabras para cifrarlas y las guarda en un archivo."""
    cadena = input("Ingresá la palabra a codificar: ")
    cadena_original = cadena
    while cadena != "FIN": # Si la palabra es "FIN", termina el programa
        encripto(cadena, False) 
        print("La cadena cifrada ha sido guardada en el archivo 'texto.txt'.") 
        guardar_original(cadena_original)
        cadena = input("Ingresá la palabra a codificar: ")
        cadena_original = cadena
    mostrar_resultados()


if __name__ == "__main__":
    """Ejecuta el programa principal"""
    main()
