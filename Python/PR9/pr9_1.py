import csv

input_file = "exports.csv"
output_file = "exports_result.csv"

try:
    with open(input_file, "r", encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile)

        # шукаємо колонку для 2019 року
        year_column = None
        for field in reader.fieldnames:
            if "2019" in field:
                year_column = field
                break

        if not year_column:
            print("У файлі немає колонки з 2019 роком!")
            exit()

        data = []
        print(f"Country Name: {year_column}")

        for row in reader:
            country = row["Country Name"]
            value = row.get(year_column, "")

            # перевіряємо, щоб значення було числовим (іноді у World Bank буває "..")
            try:
                value = float(value)
                data.append((country, value))
                print(f"{country}: {value}")
            except:
                continue  # пропускаємо пусті або некоректні значення

        if not data:
            print("Дані за 2019 рік відсутні у файлі.")
        else:
            # знаходимо мінімум і максимум
            min_country, min_value = min(data, key=lambda x: x[1])
            max_country, max_value = max(data, key=lambda x: x[1])

            print("\nМінімальне значення:", min_country, ":", min_value)
            print("Максимальне значення:", max_country, ":", max_value)

            # зберігаємо у новий CSV
            with open(output_file, "w", newline="", encoding="utf-8") as csvfile2:
                writer = csv.writer(csvfile2, delimiter=";")
                writer.writerow(["Type", "Country", "Value"])
                writer.writerow(["Мінімальне", min_country, min_value])
                writer.writerow(["Максимальне", max_country, max_value])

            print(f"\nРезультат збережено у файл {output_file}")

except FileNotFoundError:
    print(f"Файл {input_file} не знайдено!")
except Exception as e:
    print("Сталася помилка при обробці:", e)
