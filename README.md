# Battery Discharge Model 🔋📉

Este repositorio contiene un modelo simplificado de descarga de una batería de ion-litio implementado en Python.

## Descripción

Se simula el voltaje de una batería en función del tiempo durante una descarga constante. El modelo considera:

- Capacidad nominal (Ah)
- Voltaje de carga completa y mínima
- Resistencia interna
- Corriente constante de descarga

## Parámetros

- Voltaje inicial: 4.2 V  
- Voltaje mínimo: 3.0 V  
- Capacidad: 2.5 Ah  
- Corriente de descarga: 1 A  
- Resistencia interna: 0.05 Ω  
- Tiempo de simulación: 1 hora

## Ejecución

```bash
python battery_model.py
