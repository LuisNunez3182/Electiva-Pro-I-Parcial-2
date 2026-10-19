estudiantes = [
    {"nombre": "Ana", "nota": 85},
    {"nombre": "Carlos", "nota": 92},
    {"nombre": "Beatriz", "nota": 78}
]

# Ordenar de menor a mayor calificación según la clave 'nota'
estudiantes_ordenados = sorted(estudiantes, key=lambda est: est["nota"])
print(estudiantes_ordenados)
