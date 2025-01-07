import numpy as np
import matplotlib.pyplot as plt

# Definimos el rango de tiempo
t = np.linspace(0, 2, 400)

# Definimos las funciones para la posición, velocidad y aceleración
def x(t):
    return 2.17 + 4.80 * t**2 - 0.100 * t**6

def v(t):
    return 9.60 * t - 0.600 * t**5

def a(t):
    return 9.60 - 3.00 * t**4

# Calculamos los valores de x, v y a
x_values = x(t)
v_values = v(t)
a_values = a(t)

# Crear las gráficas
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12))

# Gráfica x-t
ax1.plot(t, x_values, label='x(t)')
ax1.set_title('Gráfica x-t')
ax1.set_xlabel('Tiempo (s)')
ax1.set_ylabel('Posición (m)')
ax1.grid(True)
ax1.legend()

# Gráfica v-t
ax2.plot(t, v_values, label='v(t)', color='orange')
ax2.set_title('Gráfica v-t')
ax2.set_xlabel('Tiempo (s)')
ax2.set_ylabel('Velocidad (m/s)')
ax2.grid(True)
ax2.legend()

# Gráfica a-t
ax3.plot(t, a_values, label='a(t)', color='green')
ax3.set_title('Gráfica a-t')
ax3.set_xlabel('Tiempo (s)')
ax3.set_ylabel('Aceleración (m/s^2)')
ax3.grid(True)
ax3.legend()

# Mostrar las gráficas
plt.tight_layout()
plt.show()
