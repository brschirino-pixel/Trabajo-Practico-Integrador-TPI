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
def filtrar_por_continente():
    
    continente_buscado = input("Ingrese el continente a filtrar: ").strip().capitalize()

    while continente_buscado == "":
        print("Error. El continente no puede estar vacío.")
        continente_buscado = input("Ingrese el continente nuevamente: ").strip().capitalize()
    
    encontrados = False

    print("\nPaíses encontrados:\n")

    for i in range(len(nombre_lista)):

        if continente_lista[i] == continente_buscado:

            print(f"Nombre: {nombre_lista[i]}")
            print(f"Población: {poblacion_lista[i]}")
            print(f"Superficie: {superficie_lista[i]} km²")
            print(f"Continente: {continente_lista[i]}")
            print("---------------------------")

            encontrados = True

    if encontrados == False:
        print("No se encontraron países en ese continente.")

def filtrar_por_rango_poblacion():
    
    minimo = input("Ingrese la población mínima: ").strip()

    while not minimo.isdigit() or int(minimo) < 0:
        print("Error. Ingrese solo números positivos.")
        minimo = input("Ingrese la población mínima nuevamente: ").strip()

    maximo = input("Ingrese la población máxima: ").strip()

    while not maximo.isdigit() or int(maximo) < 0:
        print("Error. Ingrese solo números positivos.")
        maximo = input("Ingrese la población máxima nuevamente: ").strip()

    minimo = int(minimo)
    maximo = int(maximo)

    while minimo > maximo:

        print("Error. El mínimo no puede ser mayor al máximo.")

    minimo = int(input("Ingrese nuevamente la población mínima: "))
    maximo = int(input("Ingrese nuevamente la población máxima: "))

    encontrados = False

    print("\nPaíses encontrados:\n")

    for i in range(len(nombre_lista)):

        if poblacion_lista[i] >= minimo and poblacion_lista[i] <= maximo:

            print(f"Nombre: {nombre_lista[i]}")
            print(f"Población: {poblacion_lista[i]}")
            print(f"Superficie: {superficie_lista[i]} km²")
            print(f"Continente: {continente_lista[i]}")
            print("---------------------------")

            encontrados = True

    if encontrados == False:
        print("No se encontraron países en ese rango de población.")

def filtrar_por_rango_superficie():
    
    minimo = input("Ingrese la superficie mínima: ").strip()

    while not minimo.isdigit() or int(minimo) < 0:
        print("Error. Ingrese solo números positivos.")
        minimo = input("Ingrese la superficie mínima nuevamente: ").strip()

    maximo = input("Ingrese la superficie máxima: ").strip()

    while not maximo.isdigit() or int(maximo) < 0:
        print("Error. Ingrese solo números positivos.")
        maximo = input("Ingrese la superficie máxima nuevamente: ").strip()

    minimo = int(minimo)
    maximo = int(maximo)

    while minimo > maximo:

        print("Error. El mínimo no puede ser mayor al máximo.")

        minimo = int(input("Ingrese nuevamente la superficie mínima: "))
        maximo = int(input("Ingrese nuevamente la superficie máxima: "))

    encontrados = False

    print("\nPaíses encontrados:\n")

    for i in range(len(nombre_lista)):

        if superficie_lista[i] >= minimo and superficie_lista[i] <= maximo:

            print(f"Nombre: {nombre_lista[i]}")
            print(f"Superficie: {superficie_lista[i]} km²")
            print(f"Población: {poblacion_lista[i]}")
            print(f"Continente: {continente_lista[i]}")
            print("---------------------------")

            encontrados = True

    if encontrados == False:
        print("No se encontraron países en ese rango de superficie.")

def ordenar_por_nombre():
    
    orden = input("Ingrese 'asc' para ascendente o 'desc' para descendente: ").strip().lower()

    while orden != "asc" and orden != "desc":
        print("Error. Debe ingresar 'asc' o 'desc'.")
        orden = input("Ingrese nuevamente el orden: ").strip().lower()
    
    for i in range(len(nombre_lista)):

        for j in range(i + 1, len(nombre_lista)):

            if (orden == "asc" and nombre_lista[i] > nombre_lista[j]) or (orden == "desc" and nombre_lista[i] < nombre_lista[j]):

                nombre_lista[i], nombre_lista[j] = nombre_lista[j], nombre_lista[i]

                poblacion_lista[i], poblacion_lista[j] = poblacion_lista[j], poblacion_lista[i]

                superficie_lista[i], superficie_lista[j] = superficie_lista[j], superficie_lista[i]

                continente_lista[i], continente_lista[j] = continente_lista[j], continente_lista[i]

    print("\nPaíses ordenados por nombre:\n")

    for i in range(len(nombre_lista)):

        print(f"Nombre: {nombre_lista[i]}")
        print(f"Población: {poblacion_lista[i]}")
        print(f"Superficie: {superficie_lista[i]} km²")
        print(f"Continente: {continente_lista[i]}")
        print("---------------------------")

def ordenar_por_poblacion():
    
    orden = input("Ingrese 'asc' para ascendente o 'desc' para descendente: ").strip().lower()

    while orden != "asc" and orden != "desc":
        print("Error. Debe ingresar 'asc' o 'desc'.")
        orden = input("Ingrese nuevamente el orden: ").strip().lower()

    for i in range(len(poblacion_lista)):

        for j in range(i + 1, len(poblacion_lista)):

            if (orden == "asc" and poblacion_lista[i] > poblacion_lista[j]) or (orden == "desc" and poblacion_lista[i] < poblacion_lista[j]):

                poblacion_lista[i], poblacion_lista[j] = poblacion_lista[j], poblacion_lista[i]

                nombre_lista[i], nombre_lista[j] = nombre_lista[j], nombre_lista[i]

                superficie_lista[i], superficie_lista[j] = superficie_lista[j], superficie_lista[i]

                continente_lista[i], continente_lista[j] = continente_lista[j], continente_lista[i]

    print("\nPaíses ordenados por población:\n")

    for i in range(len(nombre_lista)):

        print(f"Nombre: {nombre_lista[i]}")
        print(f"Población: {poblacion_lista[i]}")
        print(f"Superficie: {superficie_lista[i]} km²")
        print(f"Continente: {continente_lista[i]}")
        print("---------------------------")

def ordenar_por_superficie():
    
    orden = input("Ingrese 'asc' para ascendente o 'desc' para descendente: ").strip().lower()

    while orden != "asc" and orden != "desc":
        print("Error. Debe ingresar 'asc' o 'desc'.")
        orden = input("Ingrese nuevamente el orden: ").strip().lower()
    
    for i in range(len(superficie_lista)):

        for j in range(i + 1, len(superficie_lista)):

            if (orden == "asc" and superficie_lista[i] > superficie_lista[j]) or (orden == "desc" and superficie_lista[i] < superficie_lista[j]):

                superficie_lista[i], superficie_lista[j] = superficie_lista[j], superficie_lista[i]

                nombre_lista[i], nombre_lista[j] = nombre_lista[j], nombre_lista[i]

                poblacion_lista[i], poblacion_lista[j] = poblacion_lista[j], poblacion_lista[i]

                continente_lista[i], continente_lista[j] = continente_lista[j], continente_lista[i]

    print("\nPaíses ordenados por superficie:\n")

    for i in range(len(nombre_lista)):

        print(f"Nombre: {nombre_lista[i]}")
        print(f"Población: {poblacion_lista[i]}")
        print(f"Superficie: {superficie_lista[i]} km²")
        print(f"Continente: {continente_lista[i]}")
        print("---------------------------")

# Estadisticas:
def mayor_y_menor_poblacion():
    
    if len(poblacion_lista) == 0:
        print("No hay países cargados.")
        return
    
    mayor = max(poblacion_lista)
    menor = min(poblacion_lista)

    indice_mayor = poblacion_lista.index(mayor)
    indice_menor = poblacion_lista.index(menor)

    print("\nPaís con MAYOR población:")
    print(f"{nombre_lista[indice_mayor]} - {mayor} habitantes")

    print("\nPaís con MENOR población:")
    print(f"{nombre_lista[indice_menor]} - {menor} habitantes")

def promedio_poblacion():
    
    if len(poblacion_lista) == 0:
        print("No hay países cargados.")
        return
    
    suma = 0

    for poblacion in poblacion_lista:
        suma += poblacion

    promedio = suma / len(poblacion_lista)

    print(f"\nEl promedio de población es: {promedio}")

def promedio_superficie():
    
    if len(superficie_lista) == 0:
        print("No hay países cargados.")
        return

    suma = 0

    for superficie in superficie_lista:
        suma += superficie

    promedio = suma / len(superficie_lista)

    print(f"\nEl promedio de superficie es: {promedio} km²")

def cantidad_paises_por_continente():
    
    africa = 0
    america = 0
    asia = 0
    europa = 0
    oceania = 0

    for continente in continente_lista:

        if continente == "África" or continente == "Africa":
            africa += 1

        elif continente == "América" or continente == "America":
            america += 1

        elif continente == "Asia":
            asia += 1

        elif continente == "Europa":
            europa += 1

        elif continente == "Oceanía" or continente == "Oceania":
            oceania += 1

    print("\nCantidad de países por continente:")
    print(f"África: {africa}")
    print(f"América: {america}")
    print(f"Asia: {asia}")
    print(f"Europa: {europa}")
    print(f"Oceanía: {oceania}")

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
    while not (continente.isalpha() and continente != "" and len(continente) <= 50 and continente in continentes_validos):
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

# Importar la biblioteca para trabajar con archivos csv.
import csv

# Leer el archivo
with open("datos.csv", mode="r", encoding="utf-8") as archivo:
    lector_csv = csv.DictReader(archivo)
    for fila in lector_csv:
        if len(fila) == 4:  # Verificar que la fila tenga 4 elementos
            nombre_lista.append(fila["nombre"])
            poblacion_lista.append(int(fila["poblacion"]))
            superficie_lista.append(int(fila["superficie"]))
            continente_lista.append(fila["continente"])
        
# Prueba ingreso de datos:
print("Ingrese los datos del país:")
pais(nombre, poblacion, superficie, continente)
print("Datos ingresados:")
print(f"Nombre: {nombre_lista[-1]}")
print(f"Población: {poblacion_lista[-1]} habitantes")
print(f"Superficie: {superficie_lista[-1]} km²")
print(f"Continente: {continente_lista[-1]}")

# Prueba de listas:
print("\nListas actualizadas:")
print(f"Nombres: {nombre_lista}")
print(f"Poblaciones: {poblacion_lista}")    
print(f"Superficies: {superficie_lista} km²")
print(f"Continentes: {continente_lista}")

filtrar_por_continente()
# filtrar_por_rango_poblacion()
# ordenar_por_nombre()
# promedio_poblacion()