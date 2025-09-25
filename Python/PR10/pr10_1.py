import matplotlib.pyplot as plt
import numpy as np

# Діапазон значень x (починаємо з 0.01, щоб уникнути ділення на 0)
x = np.linspace(0.01, 4, 400)

# Функція Y(x) = (sin(10x) * sin(3x)) / x^2
y = (np.sin(10 * x) * np.sin(3 * x)) / (x**2)

# Побудова графіка
plt.plot(x, y, label='Y(x) = sin(10x)*sin(3x)/x^2',
         color='green', linewidth=2, linestyle='-')

# Заголовок та підписи осей
plt.title('Графік функції Y(x)', fontsize=15)
plt.xlabel('x', fontsize=12, color='blue')
plt.ylabel('Y(x)', fontsize=12, color='blue')

# Легенда та сітка
plt.legend()
plt.grid(True)

# Відображення графіка
plt.show()
