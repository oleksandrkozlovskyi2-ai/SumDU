# Завдання 2. Обробка слів
word1 = str(input("Введіть перше слово: "))
word2 = str(input("Введіть друге слово: "))

result = []

for ch in word1:
    if word1.count(ch) == 1 and word2.count(ch) == 1 and ch in word2:
        result.append(ch)

if result:
    print("Літери, які зустрічаються в обох словах лише один раз:", " ".join(result))
else:
    print("Немає спільних літер, які зустрічаються тільки один раз.")
