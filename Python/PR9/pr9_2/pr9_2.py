import json
import os

DATA_FILE = "weather.json"
RESULT_FILE = "weather_result.json"

# початкові дані
weather_data = [
    {"day": 1, "precipitation": 5, "temperature": -2},
    {"day": 2, "precipitation": 0, "temperature": 1},
    {"day": 3, "precipitation": 12, "temperature": 3},
    {"day": 4, "precipitation": 7, "temperature": -1}
]

# створюємо файл, якщо він ще не існує
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(weather_data, f, ensure_ascii=False, indent=4)


def load_data():
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def view_data():
    data = load_data()
    print("\nДані про погоду:")
    for record in data:
        print(record)


def add_record():
    data = load_data()
    day = int(input("День: "))
    precipitation = float(input("Кількість опадів (мм): "))
    temperature = float(input("Температура (°C): "))
    data.append({"day": day, "precipitation": precipitation, "temperature": temperature})
    save_data(data)
    print("Запис додано!")


def delete_record():
    data = load_data()
    day = int(input("Вкажіть день для видалення: "))
    data = [rec for rec in data if rec["day"] != day]
    save_data(data)
    print("Запис видалено!")


def search_record():
    data = load_data()
    day = int(input("Вкажіть день для пошуку: "))
    result = [rec for rec in data if rec["day"] == day]
    if result:
        print("Знайдено:", result[0])
    else:
        print("Дані за цей день відсутні.")


def calculate_snow_rain():
    data = load_data()
    snow = sum(rec["precipitation"] for rec in data if rec["temperature"] <= 0)
    rain = sum(rec["precipitation"] for rec in data if rec["temperature"] > 0)

    result = {"Сніг": snow, "Дощ": rain}
    print("\nРезультат обчислень:", result)

    with open(RESULT_FILE, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
    print(f"Результати збережено у {RESULT_FILE}")


# --- головне меню ---
while True:
    print("\nМеню:")
    print("1 - Переглянути дані")
    print("2 - Додати запис")
    print("3 - Видалити запис")
    print("4 - Пошук по дню")
    print("5 - Обчислити (сніг/дощ) і зберегти результат")
    print("6 - Вихід")

    choice = input("Ваш вибір: ")

    if choice == "1":
        view_data()
    elif choice == "2":
        add_record()
    elif choice == "3":
        delete_record()
    elif choice == "4":
        search_record()
    elif choice == "5":
        calculate_snow_rain()
    elif choice == "6":
        break
    else:
        print("Невірний вибір!")
