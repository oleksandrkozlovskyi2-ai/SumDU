import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Завантаження CSV
df = pd.read_csv("API_SE.csv", skiprows=4)

# Рік
year = "2021"

# Дані по країнах
ukraine_value = df[df["Country Name"] == "Ukraine"][year].values[0]
usa_value = df[df["Country Name"] == "United States"][year].values[0]

# Перетворюємо в числа і замінюємо NaN на 0
values = [ukraine_value, usa_value]
values = [0 if pd.isna(v) else float(v) for v in values]

labels = ["Ukraine", "USA"]
colors = ["skyblue", "lightgreen"]

# Перевіримо, чи є хоч якісь дані
if sum(values) == 0:
    print(f"Немає даних для {year}")
else:
    plt.figure(figsize=(6,6))
    plt.pie(values,
            labels=labels,
            autopct='%1.1f%%',
            colors=colors,
            startangle=90)
    plt.title(f"Children out of school, primary in {year}", fontsize=14)
    plt.show()

