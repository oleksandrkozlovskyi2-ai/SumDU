# Завдання 3. Варіант 7

N = int(input("Введіть число N (1 < N < 9): "))

while N <= 1 or N >= 9:   # перевірка умови
    N = int(input("Введіть ще раз N (1 < N < 9): "))

# побудова рисунку
for i in range(1, N + 1):       # рядки
    for j in range(i, N + 1):   # числа в рядку
        print(j, end=" ")
    print()
