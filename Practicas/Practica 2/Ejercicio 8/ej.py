#Escriba un programa que solicite que se ingrese una palabra o frase y permita identificar si la
#misma es un Heterograma (tenga en cuenta que el contenido del enlace es una traducción del
#inglés por lo cual las palabras que nombra no son heterogramas en español). Un Heterograma es
#una palabra o frase que no tiene ninguna letra repetida entre sus caracteres. 

is_heterogram = True

def main():
    cadena = input("Ingrese una palabra o frase: ").lower()
    for char in cadena:
        if cadena.count(char) < 1:
            is_heterogram = True
        else:
            is_heterogram = False
        break
    if is_heterogram == True:
        print(f"La palabra {cadena} es un heterograma")
    else:
        print(f"La palabra {cadena} no es un heterograma")

        
if __name__ == "__main__":
    main()

