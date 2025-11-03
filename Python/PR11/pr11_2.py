import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Завантаження даних
df = pd.read_csv('comptage_velo_2019.csv')

# Перевірка основних характеристик датафрейму
print("Перші 5 рядків датафрейму:")
print(df.head())
print("\n" + "="*50 + "\n")

print("Інформація про датафрейм:")
print(df.info())
print("\n" + "="*50 + "\n")

print("Статистичний опис даних:")
print(df.describe())
print("\n" + "="*50 + "\n")

# Перетворення стовпця дати у datetime формат
df['date'] = pd.to_datetime(df['date'])
df['heure'] = pd.to_timedelta(df['heure'])

# Додавання стовпців для місяця та дня тижня для подальшого аналізу
df['month'] = df['date'].dt.month
df['day_of_week'] = df['date'].dt.day_name()

# 1. Загальна кількість велосипедистів за рік на усіх велодоріжках
total_cyclists_year = df['nb_passages'].sum()
print(f"Загальна кількість велосипедистів за 2019 рік: {total_cyclists_year}")
print("\n" + "="*50 + "\n")

# 2. Загальна кількість велосипедистів за рік на кожній велодоріжці
cyclists_per_counter = df.groupby('id_compteur')['nb_passages'].sum().sort_values(ascending=False)
print("Кількість велосипедистів на кожній велодоріжці:")
print(cyclists_per_counter)
print("\n" + "="*50 + "\n")

# 3. Вибір трьох найпопулярніших велодоріжок для аналізу
top_counters = cyclists_per_counter.head(3).index.tolist()
print(f"Три найпопулярніші велодоріжки: {top_counters}")

# Аналіз найпопулярнішого місяця для кожної з трьох велодоріжок
print("\nНайпопулярніші місяці для трьох основних велодоріжок:")
for counter_id in top_counters:
    counter_data = df[df['id_compteur'] == counter_id]
    monthly_data = counter_data.groupby('month')['nb_passages'].sum()
    most_popular_month = monthly_data.idxmax()
    month_name = pd.to_datetime(f'2019-{most_popular_month}-01').strftime('%B')
    print(f"Велодоріжка {counter_id}: найпопулярніший місяць - {month_name} ({most_popular_month}-й місяць), кількість велосипедистів: {monthly_data.max()}")
print("\n" + "="*50 + "\n")

# 4. Побудова графіка завантаженості однієї з велодоріжок по місяцям
selected_counter = top_counters[0]  # Вибираємо першу з найпопулярніших велодоріжок

# Дані для обраної велодоріжки
counter_data = df[df['id_compteur'] == selected_counter]
monthly_usage = counter_data.groupby('month')['nb_passages'].sum()

# Назви місяців для підписів на графіку
month_names = ['Січень', 'Лютий', 'Березень', 'Квітень', 'Травень', 'Червень',
              'Липень', 'Серпень', 'Вересень', 'Жовтень', 'Листопад', 'Грудень']

# Створення графіка
plt.figure(figsize=(12, 6))
bars = plt.bar(monthly_usage.index, monthly_usage.values, color='skyblue', alpha=0.7)
plt.title(f'Завантаженість велодоріжки {selected_counter} по місяцям (2019 рік)', fontsize=14, fontweight='bold')
plt.xlabel('Місяць', fontsize=12)
plt.ylabel('Кількість велосипедистів', fontsize=12)
plt.xticks(monthly_usage.index, [month_names[i-1] for i in monthly_usage.index], rotation=45)
plt.grid(axis='y', alpha=0.3)

# Додавання значень на стовпці
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}', ha='center', va='bottom')

plt.tight_layout()
plt.show()

# Додатковий аналіз: загальна статистика по місяцям для всіх велодоріжок
print("Загальна статистика використання велодоріжок по місяцям:")
monthly_total = df.groupby('month')['nb_passages'].sum()
for month, count in monthly_total.items():
    print(f"{month_names[month-1]}: {count} велосипедистів")

# Знаходження найпопулярнішого місяця в цілому
most_popular_month_total = monthly_total.idxmax()
print(f"\nНайпопулярніший місяць в цілому: {month_names[most_popular_month_total-1]} ({monthly_total.max()} велосипедистів)")
