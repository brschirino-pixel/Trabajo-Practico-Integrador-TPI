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

def validar_nombre():
    nombre = input("Ingrese el nombre del país: ").strip().capitalize()
    while not (nombre.isalpha() and nombre != "" and len(nombre) <= 50):
        print("El valor ingresado no es válido. Por favor, ingrese solo letras.")
        nombre = input("Ingrese el nombre del país nuevamente: ").strip().capitalize()
    return nombre

def validar_poblacion():
    poblacion = input("Ingrese la población del país: ").strip()
    while not (poblacion.isdigit() and poblacion != "" and int(poblacion) > 0):
        print("El valor ingresado no es válido. Por favor, ingrese un número entero positivo.")
        poblacion = input("Ingrese la población nuevamente: ").strip()
    return int(poblacion)

def validar_superficie():
    superficie = input("Ingrese la superficie del país: ").strip()
    while not (superficie.isdigit() and superficie != "" and int(superficie) > 0):
        print("El valor ingresado no es válido. Por favor, ingrese un número entero positivo.")
        superficie = input("Ingrese la superficie nuevamente: ").strip()
    return int(superficie)

def validar_continente():
    continentes_validos = ["África", "Africa","América", "America", "Asia", "Europa", "Oceanía","Oceania"]
    continente = input(f"Ingrese el continente: ").strip().capitalize()
    while continente not in continentes_validos:
        print(f"El continente ingresado no es válido. Por favor, ingrese uno de los siguientes continentes: África, América, Asia, Europa, Oceanía.")
        continente = input(f"Ingrese el continente nuevamente: ").strip().capitalize()
    return continente

# Funciones de ingreso de datos:
def pais(nombre: str, poblacion: int, superficie: int, continente: str):
    nombre = validar_nombre()
    nombre_lista.append(nombre)
    
    poblacion = validar_poblacion()
    poblacion_lista.append(poblacion)
    
    superficie = validar_superficie()
    superficie_lista.append(superficie)
    
    continente = validar_continente()
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


