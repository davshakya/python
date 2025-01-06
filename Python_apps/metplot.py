import matplotlib.pyplot as plt
import numpy as np

# 1. Line Plot
plt.figure(figsize=(10, 8))
plt.subplot(4, 4, 1)
plt.plot([1, 2, 3, 4], [10, 20, 25, 30])
plt.title('Line Plot')

# 2. Scatter Plot
plt.subplot(4, 4, 2)
plt.scatter([1, 2, 3, 4], [10, 20, 25, 30])
plt.title('Scatter Plot')

# 3. Bar Plot
plt.subplot(4, 4, 3)
plt.bar(['A', 'B', 'C'], [10, 20, 15])
plt.title('Bar Plot')

# 4. Horizontal Bar Plot
plt.subplot(4, 4, 4)
plt.barh(['A', 'B', 'C'], [10, 20, 15])
plt.title('Horizontal Bar')

# 5. Histogram
plt.subplot(4, 4, 5)
data = [10, 20, 20, 30, 30, 30, 40]
plt.hist(data, bins=4)
plt.title('Histogram')

# 6. Pie Chart
plt.subplot(4, 4, 6)
plt.pie([10, 20, 30], labels=['A', 'B', 'C'], autopct='%1.1f%%')
plt.title('Pie Chart')

# 7. Boxplot
plt.subplot(4, 4, 7)
plt.boxplot([7, 8, 8, 9, 10, 12, 13])
plt.title('Boxplot')

# 8. Area Plot
plt.subplot(4, 4, 8)
x = np.arange(0, 10, 1)
y = x ** 2
plt.fill_between(x, y, color="skyblue", alpha=0.4)
plt.plot(x, y, color="Slateblue", alpha=0.6)
plt.title('Area Plot')

# 9. Error Bars
plt.subplot(4, 4, 9)
plt.errorbar([1, 2, 3], [10, 20, 30], yerr=[1, 2, 1], fmt='o')
plt.title('Error Bars')

# 10. Stem Plot
plt.subplot(4, 4, 10)
plt.stem([1, 2, 3, 4], [10, 20, 25, 30])
plt.title('Stem Plot')

# 11. Heatmap
plt.subplot(4, 4, 11)
data = np.random.rand(5, 5)
plt.imshow(data, cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Heatmap')

# 12. Contour Plot
plt.subplot(4, 4, 12)
x = np.linspace(-3, 3, 30)
y = np.linspace(-3, 3, 30)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
plt.contour(X, Y, Z)
plt.title('Contour Plot')

# 13. Polar Plot
plt.subplot(4, 4, 13)
theta = np.linspace(0, 2*np.pi, 100)
r = np.abs(np.sin(2*theta))
plt.polar(theta, r)
plt.title('Polar Plot')

# 14. Quiver Plot
plt.subplot(4, 4, 14)
X, Y = np.meshgrid(np.arange(0, 2, 0.2), np.arange(0, 2, 0.2))
U = np.cos(X)*Y
V = np.sin(Y)*X
plt.quiver(X, Y, U, V)
plt.title('Quiver Plot')

# 15. 3D Scatter Plot
from mpl_toolkits.mplot3d import Axes3D
ax = plt.subplot(4, 4, 15, projection='3d')
ax.scatter([1, 2, 3], [1, 2, 3], [10, 20, 30])
ax.set_title('3D Scatter Plot')

# 16. Stack Plot
plt.subplot(4, 4, 16)
x = [1, 2, 3, 4]
y = [[10, 20, 30, 40], [5, 10, 15, 20]]
plt.stackplot(x, y, labels=['A', 'B'])
plt.legend()
plt.title('Stack Plot')

plt.tight_layout()
plt.show()
