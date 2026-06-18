notas = {}


def añadir_estudiante ():
    nombre = input("Ingrese el nombre del estudiante: ")
    calificacion = float(input("Ingrese la nota del estudiante: "))
    notas[nombre] = calificacion

def ver_estudiantes ():
    for nombre, calificacion in notas.items():
        print(f"{nombre}: {calificacion}")

def ver_nota_estudiante ():
    nombre = input("Ingrese el nombre del estudiante: ")
    if nombre in notas:
        print(f"{nombre}: {notas[nombre]}")
    else:
        print("Estudiante no encontrado.")


def calcular_promedio ():
    if len(notas) == 0:
        print("No hay estudiantes registrados.")
        return
    sumatorio = 0
    numero_alumnos = 0
    for nombre, calificacion in notas.items():
        sumatorio = sumatorio + calificacion
        numero_alumnos = numero_alumnos + 1
    promedio = sumatorio/numero_alumnos
    print(f"El promedio de notas es: {promedio}")

def main ():
    menu_gestor = 0
    while menu_gestor != 5:
        print("Añadir estiudiante (1)")
        print("Ver todos los estudiantes (2)")
        print("Ver nota de un estudiante (3)")
        print("Ver promedio de notas (4)")
        print("Salir (5)")
        menu_gestor = int(input("Ingrese una opción: "))
        if menu_gestor == 1:
            añadir_estudiante()
        elif menu_gestor == 2:
            ver_estudiantes()
        elif menu_gestor == 3:
            ver_nota_estudiante()
        elif menu_gestor == 4:
            calcular_promedio()
        elif menu_gestor == 5:
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente nuevamente.")
main()
