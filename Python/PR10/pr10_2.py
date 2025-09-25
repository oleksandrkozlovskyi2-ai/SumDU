import pandas as pd
import matplotlib.pyplot as plt

# Завантаження CSV, пропускаємо службові рядки
df = pd.read_csv("API_SE.csv", skiprows=4)

# Вибираємо лише потрібні колонки (2003-2022)
years = list(map(str, range(2003, 2023)))
data = df[["Country Name"] + years]

# Фільтруємо країни Україна та США
ukraine = data[data["Country Name"] == "Ukraine"].iloc[0, 1:].astype(float).values
usa = data[data["Country Name"] == "United States"].iloc[0, 1:].astype(float).values

# Лінійний графік (2.1)
plt.figure(figsize=(10,5))
plt.plot(years, ukraine, label="Ukraine", color="blue", linewidth=2)
plt.plot(years, usa, label="USA", color="green", linewidth=2)

plt.title("Children out of school, primary (2003-2022)", fontsize=15)
plt.xlabel("Year", fontsize=12, color="black")
plt.ylabel("Number of children", fontsize=12, color="black")
plt.legend()
plt.grid(True)
plt.show()

# Стовпчаста діаграма (2.2)
country = input("Введіть назву країни (Ukraine або United States): ")
if country in data["Country Name"].values:
    values = data[data["Country Name"] == country].iloc[0, 1:].astype(float).values
    plt.figure(figsize=(10,5))
    plt.bar(years, values, color="orange")
    plt.title(f"Children out of school, primary in {country}", fontsize=15)
    plt.xlabel("Year", fontsize=12, color="black")
    plt.ylabel("Number of children", fontsize=12, color="black")
    plt.show()
else:
    print("Країну не знайдено у даних.")
