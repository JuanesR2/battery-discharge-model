import numpy as np
import matplotlib.pyplot as plt

# Parámetros del modelo de descarga
V_full = 4.2        # Voltaje totalmente cargado
V_empty = 3.0       # Voltaje cuando se considera descargada
capacity = 2.5      # Capacidad en Ah
R_internal = 0.05   # Resistencia interna en ohmios

# Simulación de descarga constante
I_load = 1.0  # Corriente de descarga en amperios
dt = 1        # Paso de tiempo en segundos
t_end = 3600  # Simulación por 1 hora

steps = int(t_end / dt)
voltage = []
time = []

Q = capacity * 3600  # Capacidad en Coulombs
q_used = 0

for i in range(steps):
    t = i * dt
    q_used += I_load * dt
    soc = max(0, 1 - q_used / Q)  # Estado de carga (State of Charge)
    V_batt = V_empty + (V_full - V_empty) * soc - I_load * R_internal
    voltage.append(V_batt)
    time.append(t)

# Gráfica
plt.plot(np.array(time) / 60, voltage)
plt.xlabel("Tiempo (min)")
plt.ylabel("Voltaje de la batería (V)")
plt.title("Simulación de descarga de batería Li-Ion")
plt.grid(True)
plt.show()
