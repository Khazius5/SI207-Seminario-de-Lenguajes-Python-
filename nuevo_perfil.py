import PySimpleGUI as sg
import json
import os

PATH_BASE = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
PATH_JSON = os.path.join(PATH_BASE,  'database')

os.chdir(PATH_JSON)

def verificar_archivo():
    """Verificar si el archivo JSON existe"""
    if not os.path.exists("datos.json"):
        with open("datos.json", "w") as archivo_json:
            json.dump([], archivo_json)
        return open("datos.json", "r+")
    else:
        return open("datos.json", "r+")





def agregar_usuario(alias, nombre, fecha_nac, sexo):
    """Agregar un usuario al archivo JSON"""
    nuevo_usuario = {
        "Alias": alias,
        "Nombre": nombre,
        "Fecha de nacimiento": fecha_nac,
        "Sexo": sexo
    }
    
    with verificar_archivo() as archivo:
        datos = json.load(archivo)
        
        # Obtenemos la lista de usuarios directamente del archivo
        lista_usuarios = datos
        
        # Agregamos el nuevo usuario a la lista
        lista_usuarios.append(nuevo_usuario)
        
        archivo.seek(0)  # Regresamos al inicio del archivo
        json.dump(lista_usuarios, archivo)  # Guardamos la lista actualizada en el archivo



def es_igual(alias,nombre,fecha_nac,sexo):
     # Abrir el archivo JSON y cargar los datos en una lista de diccionarios
     with open("datos.json", "r") as archivo:
        datos = json.load(archivo) #esto es un diccionario
     # Verificar si algún diccionario en la lista tiene un valor 'alias' que contenga la cadena 'alias'
     if any(alias.lower() in diccionario.values() for diccionario in datos):
        sg.popup(f"El alias '{alias}' ya existe!")
        return
     else:
        agregar_usuario(alias,nombre,fecha_nac,sexo)
        sg.popup(f"Usuario '{alias}' agregado correctamente.")



options = ['Masculino','Femenino']

layout = [
    [sg.Text("Nick o Alias")],
    [sg.Input(key= "--ALIAS--", size=(30,3)) ],
    [sg.Text("Nombre")],
    [sg.Input(key="--NOMBRE--", size=(30,3))],
    [sg.Text("Fecha_nacimiento")],
    [sg.Input(key="--FECHA_NAC--", size=(30,3))],
    [sg.Text("Genero Autopercibido")],
    [sg.Combo(options,key="--GEN--", size=(20,3))],
    [sg.Checkbox('Otro', default=False, key='--OTRO--', enable_events=True)],
    [sg.Input(key="--INPUT-OTRO--", disabled=True)],
    [sg.Button("Guardar", key="--GUARDAR--")],
    [sg.Button("Cancelar", key="--CANCELAR--")]
    ]

# asigno el layout a la ventana "windows"
window = sg.Window('Nuevo perfil', layout, size=(None, None),
                   element_justification='center', margins=(100, 100))

while True:
    JSON = verificar_archivo()
    evento, valores = window.read()
    if evento == sg.WINDOW_CLOSED:
        break

    if evento == '--OTRO--':
        if valores['--OTRO--']:
            window['--INPUT-OTRO--'].update(disabled=False)
        else:
            window['--INPUT-OTRO--'].update(disabled=True)
            window['--INPUT-OTRO--'].update('')
        sexo = valores['--INPUT-OTRO--']
    else:
        sexo = valores['--GEN--']

    if evento == "--GUARDAR--":
        es_igual(valores["--ALIAS--"],valores['--NOMBRE--'],valores['--FECHA_NAC--'],sexo) #verifica si el alias ya existe

    if evento == "--CANCELAR--":
        sg.popup("La operation fue cancelada")
        window.close()

window.close()
