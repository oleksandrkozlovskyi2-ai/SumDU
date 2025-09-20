# Варіант 7. Опади та температура
# Використання словника для зберігання даних

weather = {
    1: (5, -3),
    2: (0, 2),
    3: (8, -1),
    4: (12, 3),
    5: (7, -5),
    6: (10, 4),
    7: (0, -2),
    8: (15, 1),
    9: (9, -4),
    10: (6, 2)
}

# === Функції ===
def Print(data):
    for day in data:
        print("День", day, ":", data[day][0], "мм,", data[day][1], "°C")

def add(data, key, rain, temp):
    data[key] = (rain, temp)
    print("Добавлено день", key, ":", rain, "мм,", temp, "°C")

def Del(data, key):
    try:
        del data[key]
        print("Видалено день", key)
    except KeyError:
        print("❌ Даних за день", key, "немає у словнику!")

def print_sort(data):
    data_sorted = {k: data[k] for k in sorted(data)}
    print("\nСловник за відсортованими днями:")
    for day in data_sorted:
        print("День", day, ":", data_sorted[day][0], "мм,", data_sorted[day][1], "°C")

def calc_precipitation(data):
    snow = 0
    rain_total = 0
    for rain, temp in data.values():
        if temp <= 0:
            snow += rain
        else:
            rain_total += rain
    print("\nЗагалом сніг:", snow, "мм")
    print("Загалом дощ:", rain_total, "мм")


# === ГОЛОВНЕ МЕНЮ ===
while True:
    print("\nЯкщо ви бажаєте виведення усіх значень словника, тоді натисніть -> 1 <-")
    print("Якщо ви бажаєте додати новий запис до словника, тоді натисніть -> 2 <-")
    print("Якщо ви бажаєте видалення запису із словника, тоді натисніть -> 3 <-")
    print("Якщо ви бажаєте перегляд вмісту словника за відсортованими ключами, тоді натисніть -> 4 <-")
    print("Якщо ви бажаєте визначити кількість снігу і дощу, тоді натисніть -> 5 <-")
    print("Якщо ви бажаєте вийти з програми, тоді натисніть -> 0 <-")

    choice = input("\nВведіть пункт меню: ")

    if choice == "1":
        Print(weather)
    elif choice == "2":
        try:
            d = int(input("Введіть номер дня: "))
            r = int(input("Введіть кількість опадів (мм): "))
            t = int(input("Введіть температуру (°C): "))
            add(weather, d, r, t)
        except ValueError:
            print("❌ Помилка вводу!")
    elif choice == "3":
        try:
            d = int(input("Введіть номер дня для видалення: "))
            Del(weather, d)
        except ValueError:
            print("❌ Помилка вводу!")
    elif choice == "4":
        print_sort(weather)
    elif choice == "5":
        calc_precipitation(weather)
    elif choice == "0":
        print("Вихід з програми...")
        break
    else:
        print("❌ Невірний пункт меню!")
