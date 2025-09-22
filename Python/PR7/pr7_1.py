def Open(file_name, mode):
    try:
        file = open(file_name, mode, encoding="utf-8")
    except:
        print("Файл", file_name, "не вдалося відкрити!")
        return None
    else:
        print("Файл", file_name, "успішно відкрито!")
        return file


# Імена файлів
file1_name = "TF10_1.txt"
file2_name = "TF10_2.txt"

# --- а) створення TF10_1.txt ---
file_1_w = Open(file1_name, "w")
if file_1_w is not None:
    file_1_w.write("Python3 is great!\n")
    file_1_w.write("File123 processing test.\n")
    file_1_w.write("Numbers 9876543210 should be removed!\n")
    file_1_w.close()
    print("Дані успішно записані у", file1_name, "\n")

# --- б) читання TF10_1.txt, видалення цифр і запис у TF10_2.txt ---
file_1_r = Open(file1_name, "r")
file_2_w = Open(file2_name, "w")

if file_1_r is not None and file_2_w is not None:
    text = file_1_r.read()

    # 1) прибираємо Windows CR, LF
    text = text.replace('\r', '').replace('\n', '')

    # 2) видаляємо цифри
    text_no_digits = ''.join(ch for ch in text if not ch.isdigit())

    # (необов'язково) подивимось перші 200 символів очищеного тексту:
    print("Очищений текст (repr, перші 200 символів):")
    print(repr(text_no_digits[:200]), "\n")

    # 3) запис по 10 символів у рядок
    for i in range(0, len(text_no_digits), 10):
        chunk = text_no_digits[i:i+10]
        file_2_w.write(chunk + "\n")

    file_1_r.close()
    file_2_w.close()
    print("Файл", file2_name, "сформовано!\n")

# --- в) читання TF10_2.txt і виведення (без обрізання пробілів) ---
file_2_r = Open(file2_name, "r")
if file_2_r is not None:
    print("Вміст TF10_2.txt (видно пробіли за допомогою repr):")
    for line in file_2_r:
        # видаляємо лише символи нового рядка, але зберігаємо пробіли
        content = line.rstrip('\r\n')
        print(repr(content), "(довжина:", len(content), ")")
    file_2_r.close()
