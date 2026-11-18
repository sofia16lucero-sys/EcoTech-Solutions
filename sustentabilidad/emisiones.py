# EJERCICIO 3 - Punto A
def calcular_emisiones_carbono(consumo_kwh, factor_emision=0.4):

    if consumo_kwh < 0:
        raise ValueError("El consumo no puede ser negativo.")

    return consumo_kwh * factor_emision


# EJERCICIO 3 - Punto B
def obtener_metricas_consumo(registros):

    total_emisiones = 0
    consumos_por_planta = {}

    for registro in registros:

        planta = registro["planta"]
        consumo = registro["consumo_kwh"]

        total_emisiones += calcular_emisiones_carbono(consumo)

        consumos_por_planta[planta] = (
            consumos_por_planta.get(planta, 0) + consumo
        )

    if consumos_por_planta:
        planta_mayor_consumo = max(
            consumos_por_planta,
            key=consumos_por_planta.get
        )
    else:
        planta_mayor_consumo = "Sin registros"

    return {
        "total_emisiones": round(total_emisiones, 2),
        "planta_mayor_consumo": planta_mayor_consumo
    }