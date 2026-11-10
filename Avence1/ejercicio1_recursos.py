# Archivo: ejercicio1_recursos.py
# Curso: Principios de Programación 1
# Sección: SCV6
# Integrante: Gustavo Guevara Fuentes
# Fecha: 10/10/2026
# Versión: 1.0
# Propósito: Calcular los recursos necesarios para una misión espacial.




# Constantes: valores establecidos para los cálculos
COMBUSTIBLE_POR_DIA = 8
RESERVA_COMBUSTIBLE = 10

OXIGENO_POR_TRIPULANTE_DIA = 2
RESERVA_OXIGENO = 5

ENERGIA_POR_DIA = 5
ENERGIA_EXPLORACION = 10

PROVISIONES_POR_TRIPULANTE_DIA = 1
RESERVA_PROVISIONES = 3

TRAYECTOS_IDA_REGRESO = 2




# Entrada de datos: información de la misión
nombre_mision = input("Ingrese el nombre de la misión: ")
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje = int(input("Ingrese la duración del viaje en días: "))




# Procesamiento: cálculo del combustible
combustible_ida = dias_viaje * COMBUSTIBLE_POR_DIA
combustible_regreso = dias_viaje * COMBUSTIBLE_POR_DIA




combustible_total = (
    combustible_ida
    + combustible_regreso
    + RESERVA_COMBUSTIBLE
)




# Procesamiento: cálculo del oxígeno
oxigeno_requerido = (
    dias_viaje
    * OXIGENO_POR_TRIPULANTE_DIA
    * TRAYECTOS_IDA_REGRESO
    * tripulantes
    + RESERVA_OXIGENO
)


# Procesamiento: cálculo de la energía
energia_requerida = (
    dias_viaje
    * ENERGIA_POR_DIA
    * TRAYECTOS_IDA_REGRESO
    + ENERGIA_EXPLORACION
)


# Procesamiento: cálculo de las provisiones
provisiones_requeridas = (
    dias_viaje
    * tripulantes
    * TRAYECTOS_IDA_REGRESO
    * PROVISIONES_POR_TRIPULANTE_DIA
    + RESERVA_PROVISIONES
)




# Salida: mostrar los resultados de la misión
print("\n--- Recursos necesarios para la misión ---")
print("Nombre de la misión:", nombre_mision)
print("Cantidad de tripulantes:", tripulantes)
print("Duración estimada del viaje:", dias_viaje, "días")
print("Combustible para la ida:", combustible_ida, "unidades")
print("Combustible para el regreso:", combustible_regreso, "unidades")
print("Reserva de combustible:", RESERVA_COMBUSTIBLE, "unidades")
print("Combustible total requerido:", combustible_total, "unidades")
print("Oxígeno requerido:", oxigeno_requerido, "unidades")
print("Energía requerida:", energia_requerida, "unidades")
print("Provisiones requeridas:", provisiones_requeridas, "unidades")