# Archivo: ejercicio8_regreso.py
# Curso: SOFT-01 Principios de Programación 1 - Sección SCV6
# Integrante: Gustavo Guevara Fuentes
# Fecha: 09/11/2026 | Versión: 1.0
# Descripción: Evalúa el regreso o la supervivencia de la tripulación.
 



# Constantes de consumo diario
CONSUMO_COMBUSTIBLE_DIA = 8
CONSUMO_OXIGENO_TRIPULANTE = 2
CONSUMO_ENERGIA_DIA = 5
CONSUMO_PROVISIONES_TRIPULANTE = 1
 



# Entrada de datos
tripulantes = int(input("Ingrese la cantidad de tripulantes: "))
dias_viaje = int(input("Ingrese la cantidad de días del viaje de ida: "))
combustible = int(input("Ingrese el combustible disponible: "))
oxigeno = int(input("Ingrese el oxígeno disponible: "))
energia = int(input("Ingrese la energía disponible: "))
provisiones = int(input("Ingrese las provisiones disponibles: "))
 



# Calcular el combustible requerido para el regreso
combustible_regreso = dias_viaje * CONSUMO_COMBUSTIBLE_DIA
dias_completados = 0
regreso_activo = True
 



# Elegir entre regreso (caso A) o tripulación varada (caso B)
if combustible >= combustible_regreso:
 



    # Simular el regreso día por día
    while dias_completados < dias_viaje and regreso_activo:
        consumo_oxigeno = tripulantes * CONSUMO_OXIGENO_TRIPULANTE
        consumo_provisiones = tripulantes * CONSUMO_PROVISIONES_TRIPULANTE
 



        # Verificar todos los recursos antes de descontar el día
        if (combustible >= CONSUMO_COMBUSTIBLE_DIA
                and oxigeno >= consumo_oxigeno
                and energia >= CONSUMO_ENERGIA_DIA
                and provisiones >= consumo_provisiones):
            combustible = combustible - CONSUMO_COMBUSTIBLE_DIA
            oxigeno = oxigeno - consumo_oxigeno
            energia = energia - CONSUMO_ENERGIA_DIA
            provisiones = provisiones - consumo_provisiones
            dias_completados = dias_completados + 1
            print("Día", dias_completados, "| Combustible:", combustible,
                  "| Oxígeno:", oxigeno, "| Energía:", energia,
                  "| Provisiones:", provisiones)
        else:
            regreso_activo = False
 



    # Mostrar resultado del regreso
    if dias_completados == dias_viaje:
        print("La tripulación regresó exitosamente a la Tierra.")
        print("Combustible restante:", combustible, "unidades")
        print("Oxígeno restante:", oxigeno, "unidades")
        print("Energía restante:", energia, "unidades")
        print("Provisiones restantes:", provisiones, "unidades")
    else:
        print("El regreso se interrumpió en el día", dias_completados + 1, ".")
        consumo_oxigeno = tripulantes * CONSUMO_OXIGENO_TRIPULANTE
        consumo_provisiones = tripulantes * CONSUMO_PROVISIONES_TRIPULANTE
        if oxigeno < consumo_oxigeno:
            print("Recurso insuficiente: oxígeno")
        if energia < CONSUMO_ENERGIA_DIA:
            print("Recurso insuficiente: energía")
        if provisiones < consumo_provisiones:
            print("Recurso insuficiente: provisiones")
        print("La tripulación no completó el regreso.")
 
else:
    # Caso B: calcular supervivencia si no hay combustible para regresar
    print("La tripulación quedó varada en el destino.")
    dias_oxigeno = oxigeno // (tripulantes * CONSUMO_OXIGENO_TRIPULANTE)
    dias_energia = energia // CONSUMO_ENERGIA_DIA
    dias_provisiones = provisiones // tripulantes
 




    # Obtener el mínimo mediante condicionales, sin min()
    supervivencia = dias_oxigeno
    if dias_energia < supervivencia:
        supervivencia = dias_energia
    if dias_provisiones < supervivencia:
        supervivencia = dias_provisiones
 



    # Identificar todos los recursos limitantes, incluidos los empates
    recursos_limitantes = ""
    if dias_oxigeno == supervivencia:
        recursos_limitantes = "oxígeno"
    if dias_energia == supervivencia:
        if recursos_limitantes == "":
            recursos_limitantes = "energía"
        else:
            recursos_limitantes = recursos_limitantes + ", energía"
    if dias_provisiones == supervivencia:
        if recursos_limitantes == "":
            recursos_limitantes = "provisiones"
        else:
            recursos_limitantes = recursos_limitantes + ", provisiones"
 
    print("Días por oxígeno:", dias_oxigeno)
    print("Días por energía:", dias_energia)
    print("Días por provisiones:", dias_provisiones)
    print("Supervivencia estimada:", supervivencia, "días")
    print("Recurso(s) limitante(s):", recursos_limitantes)

