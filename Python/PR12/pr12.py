import nltk
import string
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
import os


# Завантаження необхідних ресурсів NLTK
def download_nltk_resources():
    resources = ['punkt', 'stopwords', 'wordnet', 'averaged_perceptron_tagger']
    for resource in resources:
        try:
            nltk.download(resource, quiet=True)
        except:
            print(f"Помилка завантаження ресурсу {resource}")


# Завантаження тексту з файлу
def load_text_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Файл {file_path} не знайдено!")
        return None
    except Exception as e:
        print(f"Помилка читання файлу: {e}")
        return None


# Попередня обробка тексту
def preprocess_text(text):
    # Перетворення до нижнього регістру
    text = text.lower()

    # Видалення пунктуації
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Видалення цифр та зайвих пробілів
    text = ''.join([char for char in text if not char.isdigit()])
    text = ' '.join(text.split())

    return text


# Токенізація тексту
def tokenize_text(text):
    return word_tokenize(text)


# Видалення стоп-слів
def remove_stopwords(tokens, language='english'):
    stop_words = set(stopwords.words(language))
    # Додаткові стоп-слова
    extra_stopwords = {'said', 'would', 'could', 'also', 'us', 'may', 'might', 'shall', 'should'}
    stop_words.update(extra_stopwords)

    return [word for word in tokens if word not in stop_words and len(word) > 2]


# Лематизація слів
def lemmatize_words(tokens):
    lemmatizer = WordNetLemmatizer()
    return [lemmatizer.lemmatize(word) for word in tokens]


# Аналіз частоти слів
def analyze_frequency(tokens):
    freq_dist = {}
    for word in tokens:
        freq_dist[word] = freq_dist.get(word, 0) + 1

    # Сортування за частотою
    sorted_freq = dict(sorted(freq_dist.items(), key=lambda item: item[1], reverse=True))
    return sorted_freq


# Генерація хмари слів
def generate_wordcloud(word_freq, output_path='wordcloud.png'):
    wordcloud = WordCloud(
        width=1200,
        height=600,
        background_color='white',
        max_words=100,
        colormap='viridis'
    ).generate_from_frequencies(word_freq)

    plt.figure(figsize=(12, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud - Частота слів у тексті', fontsize=16, pad=20)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.show()

    return output_path


# Побудова графіка топ-слів (ВИПРАВЛЕНА ВЕРСІЯ)
def plot_top_words(word_freq, top_n=20, output_path='top_words.png'):
    # Беремо топ-N слів
    top_words_dict = dict(list(word_freq.items())[:top_n])

    # Розділяємо слова та частоти і ПЕРЕВЕРТАЄМО порядок
    words = list(top_words_dict.keys())[::-1]  # Reverse for correct order
    frequencies = list(top_words_dict.values())[::-1]  # Reverse for correct order

    # Створюємо графік
    plt.figure(figsize=(12, 8))

    # Створюємо горизонтальний барплот
    bars = plt.barh(words, frequencies, color='skyblue', edgecolor='black')

    # Додаємо значення на стовпці
    for bar, freq in zip(bars, frequencies):
        plt.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height() / 2,
                 f'{freq}', va='center', ha='left', fontsize=10)

    # Налаштування графіка
    plt.xlabel('Частота', fontsize=12)
    plt.ylabel('Слова', fontsize=12)
    plt.title(f'Топ-{top_n} найчастіших слів у тексті', fontsize=16, pad=20)
    plt.grid(axis='x', alpha=0.3)

    # Автоматичне налаштування розмірів
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.show()

    return output_path


# Збереження результатів
def save_results(word_freq, output_file='word_frequency.csv'):
    df = pd.DataFrame(list(word_freq.items()), columns=['Word', 'Frequency'])
    df.to_csv(output_file, index=False, encoding='utf-8')
    print(f"Результати збережено у файл: {output_file}")
    return output_file


# Головна функція програми
def main():
    print("=== Аналізатор тексту та генератор хмари слів ===\n")

    # Завантаження ресурсів NLTK
    print("Завантаження необхідних ресурсів NLTK...")
    download_nltk_resources()

    # Вибір джерела тексту
    print("\nОберіть спосіб введення тексту:")
    print("1 - Ввести текст вручну")
    print("2 - Завантажити текст з файлу")

    choice = input("Ваш вибір (1/2): ").strip()

    if choice == '1':
        text = input("Введіть текст для аналізу:\n")
    elif choice == '2':
        file_path = input("Введіть шлях до текстового файлу: ").strip()
        text = load_text_from_file(file_path)
        if text is None:
            return
    else:
        print("Невірний вибір!")
        return

    if not text.strip():
        print("Текст не може бути порожнім!")
        return

    print(f"\nДовжина вхідного тексту: {len(text)} символів")

    # Обробка тексту
    print("\n=== Етап 1: Попередня обробка тексту ===")
    processed_text = preprocess_text(text)
    print("✓ Текст оброблено")

    print("\n=== Етап 2: Токенізація ===")
    tokens = tokenize_text(processed_text)
    print(f"✓ Знайдено токенів: {len(tokens)}")

    print("\n=== Етап 3: Видалення стоп-слів ===")
    filtered_tokens = remove_stopwords(tokens)
    print(f"✓ Залишилось слів після фільтрації: {len(filtered_tokens)}")

    print("\n=== Етап 4: Лематизація ===")
    lemmatized_tokens = lemmatize_words(filtered_tokens)
    print(f"✓ Слова приведено до базової форми")

    print("\n=== Етап 5: Аналіз частоти слів ===")
    word_freq = analyze_frequency(lemmatized_tokens)
    print(f"✓ Проаналізовано унікальних слів: {len(word_freq)}")

    # Вивід статистики
    print(f"\n=== Статистика аналізу ===")
    print(f"Загальна кількість слів: {len(lemmatized_tokens)}")
    print(f"Кількість унікальних слів: {len(word_freq)}")
    print(f"\nТоп-10 найчастіших слів:")
    for i, (word, freq) in enumerate(list(word_freq.items())[:10], 1):
        print(f"{i}. '{word}': {freq} разів")

    # Візуалізація
    print("\n=== Етап 6: Генерація візуалізацій ===")

    # Хмара слів
    print("Генерація хмари слів...")
    wordcloud_path = generate_wordcloud(word_freq)
    print(f"✓ Хмару слів збережено: {wordcloud_path}")

    # Графік топ-слів
    print("Побудова графіка топ-слів...")
    top_words_path = plot_top_words(word_freq)
    print(f"✓ Графік топ-слів збережено: {top_words_path}")

    # Збереження результатів
    print("\n=== Етап 7: Збереження результатів ===")
    csv_path = save_results(word_freq)

    print(f"\n=== Аналіз завершено успішно! ===")
    print(f"Створені файли:")
    print(f"- Хмара слів: {wordcloud_path}")
    print(f"- Графік топ-слів: {top_words_path}")
    print(f"- Таблиця частот: {csv_path}")


if __name__ == "__main__":
    main()
