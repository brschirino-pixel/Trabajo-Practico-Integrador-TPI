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

def validar_continente(continente):
    continentes_validos = ["África", "Africa","América", "America", "Asia", "Europa", "Oceanía","Oceania"]
    while continente not in continentes_validos:
        print("El continente ingresado no es válido. Por favor, ingrese uno de los siguientes continentes: África, América, Asia, Europa, Oceanía.")
        continente = input("Ingrese el continente nuevamente: ").strip().capitalize()

# Funciones de ingreso de datos:
def pais(nombre: str, poblacion: int, superficie: int, continente: str):
    nombre = input("Ingrese el nombre del país: ").strip().capitalize()
    validar_texto(nombre)
    nombre_lista.append(nombre)
    poblacion = input("Ingrese la población del país en millones de habitantes: ").strip()
    validar_numero(poblacion)
    poblacion_lista.append(poblacion)
    superficie = input("Ingrese la superficie del país en km²: ").strip()
    validar_numero(superficie)
    superficie_lista.append(superficie)
    continente = input("Ingrese el continente al que pertenece el país: ").strip().capitalize() 
    validar_texto(continente)
    validar_continente(continente)
    continente_lista.append(continente)
    return nombre, poblacion, superficie, continente
    
# Prueba ingreso de datos:
print("Ingrese los datos del país:")
pais(nombre, poblacion, superficie, continente)
print("Datos ingresados:")
print(f"Nombre: {nombre_lista[-1]}")
print(f"Población: {poblacion_lista[-1]} millones de habitantes")
print(f"Superficie: {superficie_lista[-1]} km²")
print(f"Continente: {continente_lista[-1]}")

# Prueba de listas:
print("\nListas actualizadas:")
print(f"Nombres: {nombre_lista}")
print(f"Poblaciones: {poblacion_lista}")    
print(f"Superficies: {superficie_lista} km²")
print(f"Continentes: {continente_lista}")


