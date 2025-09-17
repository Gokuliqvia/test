import matplotlib.pyplot as plt
import numpy as np

# Generate spiral data
theta = np.linspace(0, 8 * np.pi, 1000)
r = np.linspace(0, 1, 1000)
x = r * np.cos(theta)
y = r * np.sin(theta)

# Create a colorful spiral
colors = plt.cm.viridis(r)

plt.figure(figsize=(6, 6))
plt.scatter(x, y, c=colors, s=10)
plt.axis('equal')
plt.title("Colorful Spiral with Matplotlib")
plt.show()
