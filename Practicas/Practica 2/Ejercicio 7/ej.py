#Dada una frase identificar mayúsculas, minúsculas y caracteres no letras y contar la cantidad de
#palabras sin distinguir entre mayúsculas y minúsculas, en la frase.

from text import TEXT as txt
import string


words = txt.split()
print(words)
count = 0
is_letter = False
for word in words:
    print(word)
    for w in word:
        if (w in string.ascii_letters):
            is_letter = True
        else:
            is_letter = False
    if (is_letter == True):
        count += 1

print(f"La cantidad de palabras en el texto es de: {count}")