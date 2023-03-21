from random import choice, randrange
from datetime import datetime 

#Operadores posibles
operators = ["+","-","*",]
#Cantidad de cuentas
times = 5
#Contador inicial de tiempo
#Esto toma la fecha y hora actual
init_time = datetime.now()

print(f"¡Veremos cuanto tardas en responder estas {times} operaciones!")
correct_answers = 0
for i in range(0, times):
    #Se eligen numeros y operadores al azar
    number_1 = randrange(10)
    number_2 = randrange(10)
    operator = choice(operators)
    while (operators == "/" and number_2 == "0"):
        number_2 = randrange(10)
    match operator:
        case "+":
            math = number_1 + number_2
        case "-":
            math = number_1 - number_2
        case "/":
            math = number_1 / number_2
        case "*":
            math = number_1 * number_2
    #Se imprime la cuenta
    print(f"{i+1}-- ¿Cuanto es {number_1} {operator} {number_2}?")
    #Le pedimos al usuario el resultado 
    result = int(input("Resultado: "))

    if (math == result):
        print("¡Respuesta Correcta!")
        correct_answers += 1
    else:
        print("Respuesta incorrecta")
    #Comparamos la respuesta del usuario con el resultado de la operación


#Al terminar toda la cantidad de cuentas por resolver. 
#Se vuelve a tomar la fecha y hora. 

end_time = datetime.now()

#Restando las fechas obtenemos el tiempo transcurrido
total_time = end_time - init_time

#Mostramos ese tiempo en segundos  
print(f"\n Tardaste {total_time.seconds} segundos.")
#Mostramos las respuestas correctas e incorrectas
print(f"Obtuviste {correct_answers} respuestas correctas y {times - correct_answers} respuestas incorrectas.") 