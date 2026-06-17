import csv

# ==================================================
# LISTAS GLOBALES
# ==================================================

nombres = []
poblaciones = []
superficies = []
continentes = []

# ==================================================
# CARGAR CSV
# ==================================================

def cargar_csv(nombre_archivo="datos.csv"):

    try:

        with open(nombre_archivo, "r", newline="", encoding="utf-8") as archivo:

            # Saltar la primera línea (encabezados)
            lector = csv.reader(archivo)

            next(lector)

            for fila in lector:

                if len(fila) == 4:
                    
                    # Guardar cada dato en su lista correspondiente
                    nombres.append(fila[0].strip())
                    poblaciones.append(int(fila[1].strip()))
                    superficies.append(int(fila[2].strip()))
                    continentes.append(fila[3].strip())

        print(f"\nSe cargaron {len(nombres)} países correctamente.")

    except FileNotFoundError:
        print("\nError. No se encontró el archivo CSV.")

    except ValueError:
        print("\nError. Hay datos inválidos en el archivo CSV.")

    except Exception as error:
        print(f"\nError inesperado: {error}")

# ==================================================
# FUNCIONES AUXILIARES
# ==================================================

def mostrar_pais(indice):

    print("\n" + "-" * 40)
    
    print(f"\nNombre: {nombres[indice]}")
    print(f"Población: {poblaciones[indice]:,} habitantes")
    print(f"Superficie: {superficies[indice]:,} km²")
    print(f"Continente: {continentes[indice]}")
    
    print("-" * 40)

def validar_orden():

    while True:

        print("\nSeleccione el tipo de orden:")

        print("1. Ascendente")
        print("2. Descendente")

        opcion = input("Ingrese una opción: ").strip()

        if opcion == "1":
            return "asc"

        elif opcion == "2":
            return "desc"

        else:
            print("Error. Elija una opción válida.")

# ==================================================
# VALIDACIONES
# ==================================================

def validar_nombre(mensaje="Ingrese el nombre del país"):

    while True:

        nombre = input(f"{mensaje}: ").strip().title()

        if nombre == "":
            print("Error. El nombre no puede estar vacío.")
            continue

        nombre_limpio = nombre.replace(" ", "").replace("-", "")

        if not nombre_limpio.isalpha():
            print("Error. El nombre solo puede contener letras, espacios y guiones.")
            continue

        if len(nombre) < 2:
            print("Error. El nombre es demasiado corto.")
            continue

        if len(nombre) > 50:
            print("Error. El nombre es demasiado largo.")
            continue     

        return nombre


def validar_poblacion(mensaje="Ingrese la población"):

    while True:

        entrada = input(f"{mensaje}: ").strip().lower()

        # Permite ingresar valores como:
        # 500 mil → 500000
        if entrada.endswith(" mil"):

            numero = entrada.replace(" mil", "")

            numero = numero.replace(".", "")
            numero = numero.replace(",", "")

            if numero.isdigit():

                return int(numero) * 1000

        # Permite ingresar:
        # 2 millones → 2000000
        elif (
            entrada.endswith(" millon")
            or entrada.endswith(" millón")
            or entrada.endswith(" millones")
        ):

            numero = (
                entrada
                .replace(" millones", "")
                .replace(" millon", "")
                .replace(" millón", "")
            )

            numero = numero.replace(".", "")
            numero = numero.replace(",", "")
            # Eliminar separadores para convertir el numero

            if numero.isdigit():

                return int(numero) * 1000000

        # Casos simples
        elif entrada in ["mil"]:

            return 1000

        elif entrada in ["millon", "millón"]:

            return 1000000

        else:

            entrada = entrada.replace(".", "")
            entrada = entrada.replace(",", "")

            if entrada.isdigit():

                numero = int(entrada)

                if numero > 0:

                    return numero

        print(
            "Error. Ingrese un valor válido "
            "(ej: 1000, 1.000, 500 mil, 2 millones)"
        )

def validar_superficie(mensaje="Ingrese la superficie"):

    while True:

        superficie = input(f"{mensaje}: ").strip()

        # Permitir formatos como:
        # 1.000 → 1000
        # 1,000 → 1000
        superficie = superficie.replace(".", "")
        superficie = superficie.replace(",", "")
        
        if not superficie.isdigit():
            print(
                "Error. Ingrese un número válido "
                "(ej: 1000, 1.000, 1,000)."
            )
            continue

        superficie = int(superficie)

        if superficie <= 0:
            print("Error. La superficie debe ser mayor a 0.")
            continue

        return superficie

def validar_continente(mensaje="Ingrese el continente"):

    continentes_validos = [
        "África",
        "América",
        "Asia",
        "Europa",
        "Oceanía"
    ]

    while True:

        print("\nContinentes disponibles:")

        for i in range(len(continentes_validos)):
            print(f"{i + 1}. {continentes_validos[i]}")

        opcion = input(f"{mensaje}: ").strip()

        if opcion.isdigit():

            opcion = int(opcion)

            if 1 <= opcion <= len(continentes_validos):
                return continentes_validos[opcion - 1]

        print("Error. Continente inválido. Seleccione una de las opciones disponibles.")

# ==================================================
# GESTIÓN DE PAÍSES
# ==================================================

# ==================================================
# MOSTRAR TODOS LOS PAÍSES
# ==================================================

def mostrar_todos_los_paises():

    print("\n--- LISTA DE PAÍSES CARGADOS ---")

    if len(nombres) == 0:

        print("No hay países cargados.")

        return

    for i in range(len(nombres)):

        print(f"\nPaís {i + 1}")

        mostrar_pais(i)

def agregar_pais():

    print("\n--- AGREGAR PAÍS ---")

    nombre = validar_nombre()

    # Verificar que el país no exista previamente
    for pais in nombres:

        if pais.lower() == nombre.lower():

            print("Error. Ese país ya existe.")
            return

    poblacion = validar_poblacion()

    superficie = validar_superficie()

    continente = validar_continente()

    # Guardar datos manteniendo sincronizadas las listas
    nombres.append(nombre)
    poblaciones.append(poblacion)
    superficies.append(superficie)
    continentes.append(continente)
    
    # Imprimir confirmacion de los datos agregados.
    print("\nPaís agregado correctamente: ")
    print(f"\nNombre: {nombre}")
    print(f"Población: {poblacion} habitantes")
    print(f"Superficie: {superficie} km²")
    print(f"Continente: {continente}")

def actualizar_pais():

    print("\n--- ACTUALIZAR PAÍS ---")

    if len(nombres) == 0:
        print("No hay países cargados.")
        return

    nombre_buscar = input("Ingrese el país a actualizar: ")

    encontrado = False

    for i in range(len(nombres)):

        if nombres[i].lower() == nombre_buscar.lower():

            print("\nPaís encontrado:")
            
            mostrar_pais(i)

            poblaciones[i] = validar_poblacion("Ingrese la nueva población")

            superficies[i] = validar_superficie("Ingrese la nueva superficie")

            print("\nDatos actualizados correctamente:")
            print(f"\nNombre: {nombres[i]}")
            print(f"Población: {poblaciones[i]} habitantes")
            print(f"Superficie: {superficies[i]} km²")
            print(f"Continente: {continentes[i]}")
            
            encontrado = True

            break

    if encontrado == False:
        print("No se encontró el país.")

def buscar_por_nombre():

    print("\n--- BUSCAR PAÍS ---")

    if len(nombres) == 0:
        print("No hay países cargados.")
        return

    busqueda = input("Ingrese el nombre del país que desea buscar: ").strip().lower()

    if busqueda == "":
        print("Error. La búsqueda no puede estar vacía.")
        return
    
    encontrados = False

    for i in range(len(nombres)):

        if busqueda in nombres[i].lower():

            mostrar_pais(i)

            encontrados = True

    if encontrados == False:
        print("No se encontraron resultados.")

# ==================================================
# FILTROS
# ==================================================

def filtrar_por_continente():

    print("\n--- FILTRAR POR CONTINENTE ---")

    continente_buscado = validar_continente()

    encontrados = False

    for i in range(len(continentes)):

        if continentes[i] == continente_buscado:

            mostrar_pais(i)

            encontrados = True

    if encontrados == False:
        print("No se encontraron países.")

def filtrar_por_rango_poblacion():

    print("\n--- FILTRAR POR RANGO DE POBLACIÓN ---")

    minimo = validar_poblacion(
        "Ingrese la población mínima"
    )

    while True:

        maximo = validar_poblacion(
            "Ingrese la población máxima"
        )

        if maximo >= minimo:
            break

        print(
            "Error. La población máxima "
            "debe ser mayor o igual al mínimo."
        )

    encontrados = False

    for i in range(len(poblaciones)):
        
        # Mostrar solo países que estén dentro del rango ingresado
        if minimo <= poblaciones[i] <= maximo:

            mostrar_pais(i)

            encontrados = True

    if not encontrados:

        print(
            "\nNo se encontraron países "
            "cuya población se encuentre en ese rango."
        )
def filtrar_por_rango_superficie():

    print("\n--- FILTRAR POR RANGO DE SUPERFICIE ---")

    
    minimo = validar_superficie(
        "Ingrese la superficie mínima"
    )

    while True:

        maximo = validar_superficie(
            "Ingrese la superficie máxima"
        )

        if maximo >= minimo:
            break

        print(
            "Error. La superficie máxima "
            "debe ser mayor o igual al mínimo."
        )

    encontrados = False

    for i in range(len(superficies)):

        # Mostrar solo países dentro del rango ingresado
        if minimo <= superficies[i] <= maximo:

            mostrar_pais(i)

            encontrados = True

    if not encontrados:

        print(
            "\nNo se encontraron países "
            "cuya superficie se encuentre en ese rango."
        )

# ==================================================
# ORDENAMIENTOS
# ==================================================

def ordenar_por_nombre():

    print("\n--- ORDENAR POR NOMBRE ---")

    orden = validar_orden()

    for i in range(len(nombres)):

        for j in range(i + 1, len(nombres)):

            # Determina cuándo intercambiar posiciones
            # según el tipo de orden elegido
            condicion = (
                (orden == "asc" and nombres[i] > nombres[j]) or
                (orden == "desc" and nombres[i] < nombres[j])
            )
            if condicion:

                nombres[i], nombres[j] = nombres[j], nombres[i]
                poblaciones[i], poblaciones[j] = poblaciones[j], poblaciones[i]
                superficies[i], superficies[j] = superficies[j], superficies[i]
                continentes[i], continentes[j] = continentes[j], continentes[i]

    print("\nPaíses ordenados correctamente.")

    for i in range(len(nombres)):
        mostrar_pais(i)

def ordenar_por_poblacion():

    print("\n--- ORDENAR POR POBLACIÓN ---")

    orden = validar_orden()

    for i in range(len(poblaciones)):

        for j in range(i + 1, len(poblaciones)):

            condicion = (
                (orden == "asc" and poblaciones[i] > poblaciones[j]) or
                (orden == "desc" and poblaciones[i] < poblaciones[j])
            )

            if condicion:

                nombres[i], nombres[j] = nombres[j], nombres[i]
                poblaciones[i], poblaciones[j] = poblaciones[j], poblaciones[i]
                superficies[i], superficies[j] = superficies[j], superficies[i]
                continentes[i], continentes[j] = continentes[j], continentes[i]

    print("\nPaíses ordenados correctamente.")

    for i in range(len(nombres)):
        mostrar_pais(i)

def ordenar_por_superficie():

    print("\n--- ORDENAR POR SUPERFICIE ---")

    orden = validar_orden()

    for i in range(len(superficies)):

        for j in range(i + 1, len(superficies)):

            # Determina cuándo intercambiar posiciones
            # según el tipo de orden elegido
            condicion = (
                (orden == "asc" and superficies[i] > superficies[j]) or
                (orden == "desc" and superficies[i] < superficies[j])
            )

            if condicion:

                nombres[i], nombres[j] = nombres[j], nombres[i]
                poblaciones[i], poblaciones[j] = poblaciones[j], poblaciones[i]
                superficies[i], superficies[j] = superficies[j], superficies[i]
                continentes[i], continentes[j] = continentes[j], continentes[i]

    print("\nPaíses ordenados correctamente.")

    for i in range(len(nombres)):
        mostrar_pais(i)

# ==================================================
# ESTADÍSTICAS
# ==================================================

def pais_mayor_menor_poblacion():

    print("\n--- MAYOR Y MENOR POBLACIÓN ---")

    if len(nombres) == 0:
        print("No hay países cargados.")
        return

    # Obtener población máxima y mínima
    mayor = max(poblaciones)
    menor = min(poblaciones)

    indice_mayor = poblaciones.index(mayor)

    indice_menor = poblaciones.index(menor)

    print("\nPaís con mayor población:")
    mostrar_pais(indice_mayor)

    print("\nPaís con menor población:")
    mostrar_pais(indice_menor)

def promedio_poblacion():

    print("\n--- PROMEDIO DE POBLACIÓN ---")

    if len(poblaciones) == 0:
        print("No hay países cargados.")
        return

    promedio = sum(poblaciones) / len(poblaciones)

    print(f"\nPromedio de población: {promedio:,.2f} habitantes")

def promedio_superficie():

    print("\n--- PROMEDIO DE SUPERFICIE ---")

    if len(superficies) == 0:
        print("No hay países cargados.")
        return

    promedio = sum(superficies) / len(superficies)

    print(f"\nPromedio de superficie: {promedio:,.2f} km²")

def cantidad_paises_por_continente():

    print("\n--- CANTIDAD DE PAÍSES POR CONTINENTE ---")

    # Contador por continente
    contador = {
        "África": 0,
        "América": 0,
        "Asia": 0,
        "Europa": 0,
        "Oceanía": 0
    }

    for continente in continentes:

        if continente in contador:
            contador[continente] += 1

    for continente, cantidad in contador.items():

        print(f"{continente}: {cantidad}")

# ==================================================
# SUBMENÚ GESTIÓN
# ==================================================

def menu_gestion():

    while True:

        print("\n" + "=" * 50)

        print("GESTIÓN DE PAÍSES")

        print("=" * 50)

        print("1. Ver países cargados")
        print("2. Agregar país")
        print("3. Actualizar país")
        print("4. Buscar país")
        print("0. Volver")

        opcion = input("\nIngrese una opción: ").strip()

        if opcion == "1":
            mostrar_todos_los_paises()

        elif opcion == "2":
            agregar_pais()

        elif opcion == "3":
            actualizar_pais()

        elif opcion == "4":
            buscar_por_nombre()

        elif opcion == "0":
            break

        else:
            print("Error. Elija una de las opciones mostradas.")

# ==================================================
# SUBMENÚ FILTROS
# ==================================================

def menu_filtros():

    while True:

        print("\n" + "=" * 50)

        print("FILTROS")

        print("=" * 50)

        print("1. Filtrar por continente")
        print("2. Filtrar por rango de población")
        print("3. Filtrar por rango de superficie")
        print("0. Volver")

        opcion = input("\nIngrese una opción: ").strip()

        if opcion == "1":
            filtrar_por_continente()

        elif opcion == "2":
            filtrar_por_rango_poblacion()

        elif opcion == "3":
            filtrar_por_rango_superficie()

        elif opcion == "0":
            break

        else:
            print("Error. Elija una de las opciones mostradas.")

# ==================================================
# SUBMENÚ ORDENAMIENTOS
# ==================================================

def menu_ordenamientos():

    while True:

        print("\n" + "=" * 50)

        print("ORDENAMIENTOS")

        print("=" * 50)

        print("1. Ordenar por nombre")
        print("2. Ordenar por población")
        print("3. Ordenar por superficie")
        print("0. Volver")

        opcion = input("\nIngrese una opción: ").strip()

        if opcion == "1":
            ordenar_por_nombre()

        elif opcion == "2":
            ordenar_por_poblacion()

        elif opcion == "3":
            ordenar_por_superficie()

        elif opcion == "0":
            break

        else:
            print("Error. Elija una de las opciones mostradas.")

# ==================================================
# SUBMENÚ ESTADÍSTICAS
# ==================================================

def menu_estadisticas():

    while True:

        print("\n" + "=" * 50)

        print("ESTADÍSTICAS")

        print("=" * 50)

        print("1. País con mayor y menor población")
        print("2. Promedio de población")
        print("3. Promedio de superficie")
        print("4. Cantidad de países por continente")
        print("0. Volver")

        opcion = input("\nIngrese una opción: ").strip()

        if opcion == "1":
            pais_mayor_menor_poblacion()

        elif opcion == "2":
            promedio_poblacion()

        elif opcion == "3":
            promedio_superficie()

        elif opcion == "4":
            cantidad_paises_por_continente()

        elif opcion == "0":
            break

        else:
            print("Error. Elija una de las opciones mostradas.")

# ==================================================
# MENÚ PRINCIPAL
# ==================================================

def mostrar_menu_principal():

    print("\n" + "=" * 50)

    print("GESTIÓN DE PAÍSES")

    print("=" * 50)

    print("1. Gestión de países")
    print("2. Filtros")
    print("3. Ordenamientos")
    print("4. Estadísticas")
    print("0. Salir")

# ==================================================
# PROGRAMA PRINCIPAL
# ==================================================

def main():

    cargar_csv()
    
    # Mantener el programa funcionando hasta salir
    while True:

        mostrar_menu_principal()

        opcion = input("\nIngrese una opción: ").strip()

        if opcion == "1":
            menu_gestion()

        elif opcion == "2":
            menu_filtros()

        elif opcion == "3":
            menu_ordenamientos()

        elif opcion == "4":
            menu_estadisticas()

        elif opcion == "0":

            print("\nPrograma finalizado.")

            break

        else:
            print("\nError. Eliga una de las opciones mostradas.")

if __name__ == "__main__":
    main()