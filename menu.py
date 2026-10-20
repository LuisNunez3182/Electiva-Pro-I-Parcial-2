# Parcial 02 - Electiva de Profundizacion I
# Menu que reune los 5 puntos del parcial en un solo programa.
# Cada punto esta en su propia funcion y el menu llama la que el usuario elija.


# Clase Estudiante (puntos 2 y 3)
# Guarda el nombre y la calificacion de un estudiante.
# Se considera aprobado si la calificacion es mayor o igual a 60.

class Estudiante:
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion

    def mostrar_informacion(self):
        print("Nombre:", self.nombre, "- Calificación:", self.calificacion)

    def verificar_estado(self):
        if self.calificacion >= 60:
            print("Estado: Aprobado")
        else:
            print("Estado: Reprobado")


# Punto 1
# Una funcion lambda es una funcion pequeña y anonima que se escribe en una sola linea.
# Recibe parametros y devuelve el resultado de una sola expresion, sin usar def ni return.

def punto1():
    # Ejemplo 1: lambda que calcula el doble de un numero.
    doble = lambda x: x * 2
    print("Doble de 5:", doble(5))
    print("Doble de 12:", doble(12))

    # Ejemplo 2: lambda como clave para ordenar una lista de diccionarios por nota.
    estudiantes = [
        {"nombre": "Ana", "nota": 85},
        {"nombre": "Carlos", "nota": 92},
        {"nombre": "Beatriz", "nota": 78}
    ]
    estudiantes_ordenados = sorted(estudiantes, key=lambda est: est["nota"])
    print("Estudiantes ordenados por nota:")
    for estudiante in estudiantes_ordenados:
        print(estudiante["nombre"], "-", estudiante["nota"])


# Punto 2
# Crea un objeto Estudiante con los datos que ingresa el usuario
# y usa sus metodos para mostrar la informacion y el estado.

def punto2():
    nombre = input("Ingrese el nombre del estudiante: ")
    calificacion = float(input("Ingrese la calificación: "))

    estudiante = Estudiante(nombre, calificacion)

    print("\n--- Información del estudiante ---")
    estudiante.mostrar_informacion()
    estudiante.verificar_estado()


# Punto 3
# Convierte la lista de diccionarios en una lista de objetos Estudiante,
# muestra todos, los aprobados, los reprobados y los ordena con una lambda.

def punto3():
    estudiantes = [
        {"nombre": "Ana", "calificacion": 85},
        {"nombre": "Luis", "calificacion": 55},
        {"nombre": "Marta", "calificacion": 75},
        {"nombre": "Jorge", "calificacion": 45},
        {"nombre": "Sara", "calificacion": 90}
    ]

    lista_estudiantes = []
    for estudiante in estudiantes:
        nuevo_estudiante = Estudiante(estudiante["nombre"], estudiante["calificacion"])
        lista_estudiantes.append(nuevo_estudiante)

    print("Todos los estudiantes:")
    for estudiante in lista_estudiantes:
        estudiante.mostrar_informacion()

    print("\nEstudiantes aprobados:")
    for estudiante in lista_estudiantes:
        if estudiante.calificacion >= 60:
            estudiante.mostrar_informacion()

    print("\nEstudiantes reprobados:")
    for estudiante in lista_estudiantes:
        if estudiante.calificacion < 60:
            estudiante.mostrar_informacion()

    print("\nEstudiantes ordenados por calificación:")
    lista_estudiantes.sort(key=lambda estudiante: estudiante.calificacion)
    for estudiante in lista_estudiantes:
        estudiante.mostrar_informacion()


# Punto 4
# Funcion que revisa si un numero es primo.
# Un numero es primo si ningun numero entre 2 y el anterior a el lo divide exactamente.

def es_primo(numero):
    if numero < 2:
        return False
    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False
    return True

# Funcion generadora que entrega los numeros primos desde 2 hasta n.
# Si n es menor que 2 muestra el mensaje y termina sin entregar ningun valor.

def generar_primos(n):
    if n < 2:
        print("No existen números primos menores que 2.")
        return
    for numero in range(2, n + 1):
        if es_primo(numero):
            yield numero

def punto4():
    n = int(input("Ingresa el límite n: "))
    primos = list(generar_primos(n))

    if len(primos) > 0:
        print(f"Números primos hasta {n}: {primos}")
        print(f"Cantidad de primos encontrados: {len(primos)}")


# Punto 5
# Funcion generadora que entrega las combinaciones de tamaño k.
# Toma cada elemento como el primero de la combinacion y lo une con las combinaciones
# de tamaño k - 1 que se pueden formar con los elementos que estan despues de el.
# Para obtener esas combinaciones la funcion se llama a si misma con una lista mas corta.
# Cuando k llega a 0 entrega una lista vacia, que es la unica combinacion de tamaño 0.

def generar_combinaciones(elementos, k):
    if k == 0:
        yield []
        return
    for i in range(len(elementos)):
        for resto in generar_combinaciones(elementos[i + 1:], k - 1):
            yield [elementos[i]] + resto

def punto5():
    elementos = []
    cantidad = int(input("¿Cuántos elementos tiene el conjunto? "))

    for i in range(cantidad):
        numero = int(input(f"Ingrese el elemento {i + 1}: "))
        elementos.append(numero)

    k = int(input("Ingresa el tamaño k de cada combinación: "))

    if k < 0 or k > len(elementos):
        print(f"No se pueden formar combinaciones de tamaño {k} con {len(elementos)} elementos.")
    else:
        print(f"Combinaciones de {elementos} con k = {k}:")
        total = 0
        for combinacion in generar_combinaciones(elementos, k):
            print(combinacion)
            total = total + 1
        print(f"Cantidad de combinaciones: {total}")


# Menu principal
# Se repite hasta que el usuario elija la opcion 0.
# La opcion se compara como texto para que una letra no detenga el programa.

opcion = ""

while opcion != "0":
    print("\n===== PARCIAL 02 =====")
    print("1. Funciones lambda")
    print("2. Clase Estudiante")
    print("3. Lista de objetos")
    print("4. Generador de números primos")
    print("5. Generador de combinaciones")
    print("0. Salir")
    opcion = input("Seleccione una opción: ")
    print()

    if opcion == "1":
        punto1()
    elif opcion == "2":
        punto2()
    elif opcion == "3":
        punto3()
    elif opcion == "4":
        punto4()
    elif opcion == "5":
        punto5()
    elif opcion == "0":
        print("Fin del programa.")
    else:
        print("Opción no válida.")
