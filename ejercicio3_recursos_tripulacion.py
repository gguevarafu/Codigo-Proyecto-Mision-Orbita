# Archivo: ejercicio3_recursos_tripulacion.py
# Curso: Principios de Programación 1
# Sección: SCV6
# Integrante: Gustavo Guevara Fuentes
# Fecha: 12/10/2026
# Versión: 1.0
# Propósito: Verificar si hay suficiente oxígeno y provisiones.




# Entrada de datos: recursos disponibles y requeridos
oxigeno_disponible = int(input("Ingrese el oxígeno disponible: "))
oxigeno_requerido = int(input("Ingrese el oxígeno requerido: "))
provisiones_disponibles = int(input("Ingrese las provisiones disponibles: "))
provisiones_requeridas = int(input("Ingrese las provisiones requeridas: "))




# Condición: verificar si ambos recursos son suficientes
if (oxigeno_disponible >= oxigeno_requerido
    and provisiones_disponibles >= provisiones_requeridas):
    print("La nave posee recursos suficientes para la tripulación.")
else:
    print("La nave no posee recursos suficientes para la tripulación.")