#Dada una frase y un string ingresados por teclado (en ese orden), genere una lista de palabras, y
#sobre ella, informe la cantidad de palabras en las que se encuentra el string. No distingir entre
#mayúsculas y minúsculas.

frase = input("Ingrese la frase: ").lower()
palabra = input("Ingrese la palabra a buscar: ").lower()

print(frase.count(palabra))