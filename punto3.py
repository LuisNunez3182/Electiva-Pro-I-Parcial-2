#Clase
class Estudiante:
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion
        
    def mostrar_informacion(self):
        print("Nombre:", self.nombre, "- calificacion: ", self.calificacion)
        
estudiantes = [
    {"nombre": "Ana", "calificacion": 85},
    {"nombre": "Luis", "calificacion": 55},
    {"nombre": "Marta", "calificacion": 75},
    {"nombre": "Jorge", "calificacion": 45},
    {"nombre": "Sara", "calificacion": 90}
]

lista_estudiantes = []

for estudiante in estudiantes:
    nuevo_estudiante = Estudiante(
        estudiante["nombre"],
        estudiante["calificacion"]
    )
    lista_estudiantes.append(nuevo_estudiante)

#Imprimir todos los estudiantes
print("Todos los estudiantes")
for estudiante in lista_estudiantes:
    estudiante.mostrar_informacion()
# Mostrar solo los estudiantes aprobados    
print("Estudiantes aprobados")
for estudiante in lista_estudiantes:
    if estudiante.calificacion >= 60:
        estudiante.mostrar_informacion()
# Mostrar solo los estudiantes reprobados.       
print("Estudiantes desaprobados")
for estudiante in lista_estudiantes:
    if estudiante.calificacion < 60:
        estudiante.mostrar_informacion()
      
# Ordenar los estudiantes por calificación usando una función lambda.        
print("Estudiantes ordenados por calificacion")
lista_estudiantes.sort(key=lambda estudiante: estudiante.calificacion)

for estudiante in lista_estudiantes:
    estudiante.mostrar_informacion()
