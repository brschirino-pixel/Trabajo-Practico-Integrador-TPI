# Listas:

nombre_lista = []
poblacion_lista = []
continente_lista = []
superficie_lista = []

# Variables globales:
nombre = ""
poblacion = 0   
superficie = 0
continente = ""

# Funciones:

# Funciones de validación de datos:

def validar_texto(texto):
    while not (texto.isalpha() and texto != "" and len(texto) <= 50):
        print("El valor ingresado no es un texto válido. Por favor, ingrese solo letras.")
        texto = input(f"Ingrese el {texto} nuevamente: ").strip()

def validar_numero(cantidad):
    while not (cantidad.isdigit() and cantidad != "" and int(cantidad) > 0):
        print("El valor ingresado no es un número válido. Por favor, ingrese un número entero positivo.")
        cantidad = input(f"Ingrese la {cantidad} nuevamente: ").strip()

# Funciones de ingreso de datos:
def pais(nombre: str, poblacion: int, superficie: int, continente: str):
    nombre = input("Ingrese el nombre del país: ").strip().capitalize()
    validar_texto(nombre)
    nombre_lista.append(nombre)
    poblacion = input("Ingrese la población del país: ").strip()
    validar_numero(poblacion)
    poblacion_lista.append(poblacion)
    superficie = input("Ingrese la superficie del país en km²: ").strip()
    validar_numero(superficie)
    superficie_lista.append(superficie)
    continente = input("Ingrese el continente al que pertenece el país: ").strip().capitalize() 
    validar_texto(continente)
    continente_lista.append(continente)
    return nombre, poblacion, superficie, continente
    




