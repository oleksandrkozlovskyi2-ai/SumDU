import nltk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import string

# Завантаження всіх необхідних ресурсів NLTK
print("Завантаження ресурсів NLTK...")
nltk.download('gutenberg')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('punkt_tab')  # Додатковий ресурс для токенізації

from nltk.corpus import gutenberg
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Завантаження тексту за варіантом
print("Завантаження тексту...")
text = gutenberg.raw('burgess-busterbrown.txt')

print("=" * 60)
print("АНАЛІЗ ТЕКСТУ: burgess-busterbrown.txt")
print("=" * 60)

# 1. Визначення кількості слів у тексті
print("Токенізація тексту...")
words = word_tokenize(text)
total_words = len(words)
print(f"1. Загальна кількість слів у тексті: {total_words}")

# 2. Знаходження 10 найбільш вживаних слів (оригінальний текст)
word_freq = Counter(words)
top_10_words = word_freq.most_common(10)

print(f"\n2. 10 найбільш вживаних слів у тексті:")
for i, (word, freq) in enumerate(top_10_words, 1):
    print(f"   {i}. '{word}': {freq} разів")

# Побудова стовпчастої діаграми для оригінального тексту
plt.figure(figsize=(15, 5))

plt.subplot(1, 2, 1)
words_orig, freqs_orig = zip(*top_10_words)
bars1 = plt.bar(words_orig, freqs_orig, color='skyblue', edgecolor='navy')
plt.title('10 найбільш вживаних слів\n(оригінальний текст)')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)

# Додавання значень на стовпці
for i, v in enumerate(freqs_orig):
    plt.text(i, v + max(freqs_orig)*0.01, str(v), ha='center', va='bottom')

# 3. Видалення стоп-слів та пунктуації
print(f"\n3. Обробка тексту:")
print("   - Видалення стоп-слів")
print("   - Видалення пунктуації")

# Отримуємо стоп-слова англійською мовою
stop_words = set(stopwords.words('english'))
# Додаємо пунктуацію до стоп-слів
stop_words.update(string.punctuation)

# Фільтруємо слова
filtered_words = [
    word.lower() for word in words
    if word.lower() not in stop_words
    and word not in string.punctuation
    and word.isalpha()  # залишаємо тільки слова, що складаються з букв
]

print(f"   Кількість слів після фільтрації: {len(filtered_words)}")

# Знаходження 10 найбільш вживаних слів після фільтрації
filtered_word_freq = Counter(filtered_words)
top_10_filtered = filtered_word_freq.most_common(10)

print(f"\n4. 10 найбільш вживаних слів після видалення стоп-слів:")
for i, (word, freq) in enumerate(top_10_filtered, 1):
    print(f"   {i}. '{word}': {freq} разів")

# Побудова стовпчастої діаграми для фільтрованого тексту
plt.subplot(1, 2, 2)
words_filt, freqs_filt = zip(*top_10_filtered)
bars2 = plt.bar(words_filt, freqs_filt, color='lightcoral', edgecolor='darkred')
plt.title('10 найбільш вживаних слів\n(після видалення стоп-слів)')
plt.xlabel('Слова')
plt.ylabel('Частота')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)

# Додавання значень на стовпці
for i, v in enumerate(freqs_filt):
    plt.text(i, v + max(freqs_filt)*0.01, str(v), ha='center', va='bottom')

plt.tight_layout()
plt.show()

# Додаткова інформація
print("\n" + "=" * 60)
print("ДОДАТКОВА ІНФОРМАЦІЯ:")
print("=" * 60)

# Унікальні слова
unique_words_orig = len(set(words))
unique_words_filt = len(set(filtered_words))
print(f"Унікальні слова в оригінальному тексті: {unique_words_orig}")
print(f"Унікальні слова після фільтрації: {unique_words_filt}")

# Слова, що зникли з топ-10 після фільтрації
original_top_words = set([word.lower() for word, _ in top_10_words])
filtered_top_words = set([word for word, _ in top_10_filtered])
disappeared_words = original_top_words - filtered_top_words

if disappeared_words:
    print(f"\nСлова, що зникли з топ-10 після фільтрації: {disappeared_words}")

# Нові слова в топ-10 після фільтрації
new_words = filtered_top_words - original_top_words
if new_words:
    print(f"Нові слова в топ-10 після фільтрації: {new_words}")

# Статистика видалення
removed_words_count = total_words - len(filtered_words)
removed_percentage = (removed_words_count / total_words) * 100
print(f"\nВидалено слів: {removed_words_count} ({removed_percentage:.1f}% від загальної кількості)")

# Топ-20 слів після фільтрації для більш детального аналізу
print(f"\nТоп-20 слів після фільтрації:")
top_20_filtered = filtered_word_freq.most_common(20)
for i, (word, freq) in enumerate(top_20_filtered, 1):
    print(f"   {i:2d}. '{word}': {freq} разів")

# Аналіз довжини тексту
print(f"\nДОВЖИНА ТЕКСТУ:")
print(f"Загальна кількість символів: {len(text)}")
print(f"Загальна кількість слів: {total_words}")
print(f"Середня довжина слова: {sum(len(word) for word in filtered_words) / len(filtered_words):.2f} символів")
