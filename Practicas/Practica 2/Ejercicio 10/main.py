#Dada una lista de nombres de estudiantes y dos listas con sus notas en un curso, escriba un
#programa que manipule dichas estructuras de datos para poder resolver los siguientes puntos:
#   A. Generar una estructura con todas las notas relacionando el nombre del estudiante con las
#       notas. Utilizar esta estructura para la resolución de los siguientes items.
#   B. Calcular el promedio de notas de cada estudiante.
#   C. Calcular el promedio general del curso.
#   D. Identificar al estudiante con la nota promedio más alta.
#   E. Identificar al estudiante con la nota más baja.

from nombres import nombres as names # Importo los nombres de los estudiantes
from notas import notas_1 as n1 # Importo las notas de los estudiantes
from notas import notas_2 as n2 # Importo las notas de los estudiantes

# A. Generar una estructura con todas las notas relacionando el nombre del estudiante con las
#       notas. Utilizar esta estructura para la resolución de los siguientes items.

def process_studens():
    """Genera una estructura con todas las notas relacionando el nombre del estudiante con las
    notas. Utilizar esta estructura para la resolución de los siguientes items."""
    notas = list(map(lambda x, y: (x, y), n1, n2))
    students = {name.replace("'","").replace(" ",""): [nota[0], nota[1]] for name, nota in zip(names.split(","), notas)}
    return students

# B. Calcular el promedio de notas de cada estudiante.

def average_student(students):
    """Calcula el promedio de notas de cada estudiante."""
    for student in students:
        students[student] = sum(students[student]) / len(students[student])
    return students

# C. Calcular el promedio general del curso.

def average_course(students):
    """Calcula el promedio general del curso."""
    return sum(students.values()) / len(students)

# D. Identificar al estudiante con la nota promedio más alta.

def best_student(students):
    """Identifica al estudiante con la nota promedio más alta."""
    return max(students, key=students.get)

# E. Identificar al estudiante con la nota más baja.

def worst_student(students):
    """Identifica al estudiante con la nota más baja."""
    return min(students, key=students.get)

def main():
    """Función principal"""
    students = process_studens()
    students = average_student(students)
    print(students)
    print(f"El promedio general del curso es de {round(average_course(students), 2)}")
    print(f"El estudiante con la nota promedio más alta es {best_student(students)}")
    print(f"El estudiante con la nota más baja es {worst_student(students)}")


if __name__ == "__main__":
    main()