from mod import even_product   # підключення власного модуля

# 1) функція для обчислення z
def expression(m):
    if m == 3:
        return "Помилка: m не може дорівнювати 3"
    if (m - 3) == 0 or (m + 3) / (m - 3) < 0:
        return "Помилка: підкореневий вираз від’ємний"
    z = ((m + 3) / (m - 3)) ** 0.5
    return z

# --- Головна програма ---
m = int(input("Введіть значення m: "))
print("Значення виразу z =", expression(m))

n = int(input("Введіть значення n: "))
print("Добуток 2*4*6*...*(2n) =", even_product(n))
