class Estudiante:
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion

    def mostrar_informacion(self):
        print("Nombre:", self.nombre)
        print("Calificación:", self.calificacion)

    def verificar_estado(self):
        if self.calificacion >= 60:
            print("Estado: Aprobado")
        else:
            print("Estado: Reprobado")


nombre = input("Ingrese el nombre del estudiante: ")
calificacion = float(input("Ingrese la calificación: "))

estudiante = Estudiante(nombre, calificacion)

print("\n--- Información del estudiante ---")
estudiante.mostrar_informacion()
estudiante.verificar_estado()
