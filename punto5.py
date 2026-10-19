# Punto 5
# Cree una función generadora que produzca todas las combinaciones posibles de un conjunto de elementos,
# dado un tamaño k.
# Por ejemplo, para el conjunto {1, 2, 3} y k = 2, las combinaciones serían: (1, 2), (1, 3), (2, 3)

# 1. Funcion generadora que entrega las combinaciones de tamaño k.
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
