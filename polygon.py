import numpy as np
import matplotlib.pyplot as plt
 
# Laufvariable t von 0 bis 360 Grad
t = np.linspace(0,2*np.pi)
 
# Maximaler Radius
ra = 6.4 / 2
ri = 5.6 / 2
rm = (ra + ri) / 2
e = 0.2

# Formeln fuer parametrische, kartesische Darstellung eines Polygons nach DIN 32711
x_t = (rm - e * np.cos(3 * t)) * np.cos(t) - 3 * e * np.sin(3 * t) * np.sin(t)
y_t = (rm - e * np.cos(3 * t)) * np.sin(t) + 3 * e * np.sin(3 * t) * np.cos(t)

plt.plot(x_t, y_t)

s = np.linspace(0,2*np.pi)
x_s = ra * np.cos(s)
y_s = ra * np.sin(s)

plt.plot(x_s, y_s)

u = np.linspace(0,2*np.pi)
x_u = ri * np.cos(u)
y_u = ri * np.sin(u)

plt.plot(x_u, y_u)

v = np.linspace(0,2*np.pi)
x_v = rm * np.cos(v)
y_v = rm * np.sin(v)

plt.plot(x_v, y_v)
plt.rcParams["figure.figsize"] = 10, 10
plt.show()

print("Da =", ra * 2)
print("Di =", ri * 2)
print("Dm =", rm * 2)
print("e =", e)