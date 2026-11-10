# Archivo: ejercicio4_lanzamiento.py
# Curso: Principios de Programación 1
# Sección: SCV6
# Integrante: [Escribe tu nombre]
# Fecha: 14/10/2026
# Versión: 1.0
# Propósito: Verificar si se puede autorizar el lanzamiento.




# Constante: reserva de emergencia de combustible
RESERVA_COMBUSTIBLE = 10




# Entrada de datos: recursos disponibles y requeridos
combustible_disponible = int(input("Ingrese el combustible disponible: "))
combustible_ida = int(input("Ingrese el combustible necesario para la ida: "))
combustible_regreso = int(input("Ingrese el combustible necesario para el regreso: "))




oxigeno_disponible = int(input("Ingrese el oxígeno disponible: "))
oxigeno_requerido = int(input("Ingrese el oxígeno requerido: "))




energia_disponible = int(input("Ingrese la energía disponible: "))
energia_requerida = int(input("Ingrese la energía requerida: "))




provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))
provisiones_requeridas = int(input("Ingrese las provisiones requeridas: "))




# Procesamiento: calcular el combustible total requerido
combustible_total = (
    combustible_ida
    + combustible_regreso
    + RESERVA_COMBUSTIBLE
)




# Condición: comprobar si todos los recursos son suficientes
if (
    combustible_disponible >= combustible_total
    and oxigeno_disponible >= oxigeno_requerido
    and energia_disponible >= energia_requerida
    and provisiones_disponibles >= provisiones_requeridas
):
    print("Lanzamiento autorizado.")
else:
    print("Lanzamiento no autorizado. La misión debe ser revisada.")