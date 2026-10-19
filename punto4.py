# Punto 4
# Cree una función generadora que produzca números primos hasta un límite n dado.
# El generador debe validar si n es menor que 2. En ese caso, debe mostrar un mensaje adecuado
# indicando que no existen números primos menores que 2.

# 1. Funcion que revisa si un numero es primo.
# Un numero es primo si ningun numero entre 2 y el anterior a el lo divide exactamente.

def es_primo(numero):
    if numero < 2:
        return False
    for divisor in range(2, numero):
        if numero % divisor == 0:
            return False
    return True

# 2. Funcion generadora que entrega los numeros primos desde 2 hasta n.
# Si n es menor que 2 muestra el mensaje y termina sin entregar ningun valor.

def generar_primos(n):
    if n < 2:
        print("No existen números primos menores que 2.")
        return
    for numero in range(2, n + 1):
        if es_primo(numero):
            yield numero


n = int(input("Ingresa el límite n: "))
primos = list(generar_primos(n))

if len(primos) > 0:
    print(f"Números primos hasta {n}: {primos}")
    print(f"Cantidad de primos encontrados: {len(primos)}")
