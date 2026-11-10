# Archivo: ejercicio2_combustible.py
# Curso: Principios de Programación 1
# Sección: SCV6
# Integrante: Gustavo Guevara Fuentes
# Fecha: 11/10/2026
# Versión: 1.0
# Propósito: Verificar la disponibilidad de combustible de la nave.




# Constante para la reserva de emergencia
RESERVA_COMBUSTIBLE = 10




# Entrada de datos: regristo del combustible
combustible_disponible = int(input("Ingrese el combustible disponible: "))
combustible_ida = int(input("Ingrese el combustible necesario para la ida: "))
combustible_regreso = int(input("Ingrese el combustible necesario para el regreso: "))




# Procesamiento: calcular el combustible total requerido
combustible_total = (
    combustible_ida
    + combustible_regreso
    + RESERVA_COMBUSTIBLE
)




# Procesamiento: calcular el combustible adicional
combustible_adicional = combustible_disponible - combustible_total




# Salida: mostrar los datos del combustible
print("\n--- Verificación de combustible ---")
print("Combustible disponible:", combustible_disponible, "unidades")
print("Combustible necesario para la ida:", combustible_ida, "unidades")
print("Combustible necesario para el regreso:", combustible_regreso, "unidades")
print("Reserva de emergencia:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Combustible adicional:", combustible_adicional, "unidades")




# Condición: advertir si el margen adicional es menor que 10
if combustible_adicional < 10:
    print("Advertencia: el margen adicional de combustible es bajo.")
