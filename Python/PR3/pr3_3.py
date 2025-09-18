# Завдання 3. Обробка рядків
sentence = str(input("Введіть речення: "))

words = sentence.split()
result = [word for word in words if "о" in word or "o" in word]

if result:
    print("Слова з літерою 'о':", ", ".join(result))
else:
    print("У реченні немає слів з літерою 'о'.")
