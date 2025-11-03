import pandas as pd

# Початкові дані
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
    10: (6, 2),
    11: (12, -1),
    12: (8, 5),
    13: (3, -3),
    14: (0, 0),
    15: (11, 2)
}

# Створення DataFrame
df = pd.DataFrame.from_dict(weather, orient='index', columns=['precipitation', 'temperature'])
df.index.name = 'day'

# Додавання нових стовпців
df['precipitation_type'] = df['temperature'].apply(lambda x: 'snow' if x <= 0 else 'rain')
df['snow_amount'] = df.apply(lambda row: row['precipitation'] if row['temperature'] <= 0 else 0, axis=1)
df['rain_amount'] = df.apply(lambda row: row['precipitation'] if row['temperature'] > 0 else 0, axis=1)

# Виведення вмісту DataFrame
print("Повний DataFrame:")
print(df)
print("\n" + "="*50 + "\n")

# Базовий аналіз даних
print("Перші 3 рядки:")
print(df.head(3))
print("\n" + "="*50 + "\n")

print("Типи даних:")
print(df.dtypes)
print("\n" + "="*50 + "\n")

print(f"Кількість рядків і стовпців: {df.shape}")
print("\n" + "="*50 + "\n")

print("Описова статистика:")
print(df.describe())
print("\n" + "="*50 + "\n")

# Фільтрація даних
print("Дні з опадами понад 8 мм:")
high_precipitation = df[df['precipitation'] > 8]
print(high_precipitation)
print("\n" + "="*50 + "\n")

# Сортування даних
print("Дні відсортовані за температурою (спадання):")
sorted_by_temp = df.sort_values('temperature', ascending=False)
print(sorted_by_temp)
print("\n" + "="*50 + "\n")

# Групування та агрегація
print("Статистика за типами опадів:")
precipitation_stats = df.groupby('precipitation_type').agg({
    'precipitation': ['count', 'sum', 'mean', 'max'],
    'temperature': ['mean', 'min', 'max']
})
print(precipitation_stats)
print("\n" + "="*50 + "\n")

# Додаткові агрегації
print("Загальна кількість опадів за типами:")
total_precipitation = df.groupby('precipitation_type')['precipitation'].sum()
print(total_precipitation)
print("\n" + "="*50 + "\n")

print("Максимальна кількість опадів за днями:")
max_precipitation_by_type = df.groupby('precipitation_type')['precipitation'].max()
print(max_precipitation_by_type)
print("\n" + "="*50 + "\n")

print("Кількість унікальних значень температури:")
unique_temps = df['temperature'].nunique()
print(f"Унікальних температур: {unique_temps}")
print("\n" + "="*50 + "\n")

# Підсумкові результати
total_snow = df['snow_amount'].sum()
total_rain = df['rain_amount'].sum()

print("РЕЗУЛЬТАТИ АНАЛІЗУ:")
print(f"Загальна кількість опадів у вигляді снігу: {total_snow} мм")
print(f"Загальна кількість опадів у вигляді дощу: {total_rain} мм")
print(f"Загальна кількість опадів: {df['precipitation'].sum()} мм")
print(f"Кількість днів зі снігом: {(df['temperature'] <= 0).sum()}")
print(f"Кількість днів з дощем: {(df['temperature'] > 0).sum()}")
