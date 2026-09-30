import numpy as np
import matplotlib.pyplot as plt

a = 9000
b = 9000

t = np.linspace(0, 2*np.pi, 10000)
x = a * np.cos(t)
y = b * np.sin(t)

plt.plot(x, y)
plt.gca().set_aspect("equal")  # so it doesn't look squished
plt.show()