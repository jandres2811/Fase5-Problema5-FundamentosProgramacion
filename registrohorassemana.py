
# Cálculo de horas semanales y clasificación de jornada laboral
# Nombre: Jorge Andres Portillo Emery
# Grupo: 213022_298
# Programa de Ingeniería de Sistemas 
# Codigo fuente: autoria propia


def clasificar_jornada(total_horas):
    if total_horas > 40:
        return "Sobretiempo"
    else:
        return "Horario estándar"


# Matriz para almacenar la información
trabajadores = []

print("=" * 50)
print("SISTEMA DE CONTROL DE HORAS LABORALES")
print("=" * 50)

# Registro de 5 trabajadores
for i in range(5):

    print(f"\nIngrese los datos del trabajador #{i+1}")

    nombre = input("Nombre del trabajador: ")

    lunes = float(input("Horas trabajadas el lunes: "))
    martes = float(input("Horas trabajadas el martes: "))
    miercoles = float(input("Horas trabajadas el miércoles: "))
    jueves = float(input("Horas trabajadas el jueves: "))
    viernes = float(input("Horas trabajadas el viernes: "))

    total_horas = lunes + martes + miercoles + jueves + viernes

    clasificacion = clasificar_jornada(total_horas)

    trabajadores.append([
        nombre,
        total_horas,
        clasificacion
    ])

    print("\nRegistro guardado correctamente.")
    input("Presione Enter para continuar...")


# Reporte final
print("\n" + "=" * 60)
print("REPORTE FINAL DE HORAS TRABAJADAS")
print("=" * 60)

for trabajador in trabajadores:
    print(f"\nNombre: {trabajador[0]}")
    print(f"Total de horas trabajadas: {trabajador[1]}")
    print(f"Clasificación: {trabajador[2]}")

print("\nReporte generado correctamente.")