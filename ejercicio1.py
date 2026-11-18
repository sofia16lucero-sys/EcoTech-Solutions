# EJERCICIO 1 - Sanitización y análisis de sensores

# Punto A
def limpiar_registro_sensor(registro_raw):
    sensor_id = registro_raw["sensor_id"].strip()

    temperatura = str(registro_raw["temperatura"]).strip()
    temperatura = temperatura.replace("°", "").replace("C", "")
    temperatura = float(temperatura)

    ubicacion = registro_raw.get("ubicacion") or "Desconocida"
    ubicacion = ubicacion.strip() or "Desconocida"

    return {
        "sensor_id": sensor_id,
        "temperatura": temperatura,
        "ubicacion": ubicacion
    }


# Punto B
def generar_resumen_sensores(lista_sensores_limpios, umbral_temperatura):
    lista_sensores_alerta = []
    suma_temperaturas = 0

    for sensor in lista_sensores_limpios:
        suma_temperaturas += sensor["temperatura"]

        if sensor["temperatura"] > umbral_temperatura:
            lista_sensores_alerta.append(sensor["sensor_id"])

    if lista_sensores_limpios:
        promedio_temperatura = suma_temperaturas / len(lista_sensores_limpios)
    else:
        promedio_temperatura = 0.0

    return lista_sensores_alerta, promedio_temperatura


# Bloque de ejecución
if __name__ == "__main__":

    registros_raw = [
        {
            "sensor_id": " SENSOR-001 ",
            "temperatura": "24.5C",
            "ubicacion": "Planta Norte"
        },
        {
            "sensor_id": " SENSOR-002 ",
            "temperatura": "35.8C",
            "ubicacion": "Planta Sur"
        },
        {
            "sensor_id": " SENSOR-003 ",
            "temperatura": "32.2C"
        },
        {
            "sensor_id": " SENSOR-004 ",
            "temperatura": "21.5C",
            "ubicacion": "Planta Este"
        }
    ]

    sensores_limpios = []

    for registro in registros_raw:
        sensores_limpios.append(limpiar_registro_sensor(registro))

    umbral = 30.0

    alertas, promedio = generar_resumen_sensores(
        sensores_limpios, umbral
    )

    print("===== REPORTE ECOTECH SOLUTIONS =====")
    print(f"Sensores analizados: {len(sensores_limpios)}")
    print(f"Umbral de temperatura: {umbral} °C")
    print(f"Temperatura promedio: {promedio:.2f} °C")
    print(f"Sensores en alerta: {len(alertas)}")

    for sensor_id in alertas:
        print(f"- {sensor_id}")