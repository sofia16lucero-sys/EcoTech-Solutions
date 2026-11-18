from django.shortcuts import render
from .emisiones import obtener_metricas_consumo


def vista_panel_sustentabilidad(request):

    registros = [
        {"planta": "Planta Norte", "consumo_kwh": 1200},
        {"planta": "Planta Sur", "consumo_kwh": 800},
        {"planta": "Planta Este", "consumo_kwh": 500},
        {"planta": "Planta Norte", "consumo_kwh": 300}
    ]

    metricas = obtener_metricas_consumo(registros)

    contexto = {
        "total_emisiones": metricas["total_emisiones"],
        "planta_mayor_consumo": metricas["planta_mayor_consumo"],
        "registros": registros
    }

    return render(
        request,
        "sustentabilidad/panel.html",
        contexto
    )