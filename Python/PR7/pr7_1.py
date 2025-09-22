def Open(file_name, mode):
    try:
        file = open(file_name, mode, encoding="utf-8")
    except:
        print("Файл", file_name, "не вдалося відкрити!")
        return None
    else:
        print("Файл", file_name, "успішно відкрито!")
        return file


# --- а) створення TF10_1.txt ---
file1_name = "TF10_1.txt"
file2_name = "TF10_2.txt"

file_1_w = Open(file1_name, "w")
if file_1_w is not None:
    file_1_w.write("Python3 is great!\n")
    file_1_w.write("File123 processing test.\n")
    file_1_w.write("Numbers 9876543210 should be removed!\n")
    file_1_w.close()
    print("Дані успішно записані у TF10_1.txt!\n")

# --- б) читання TF10_1.txt, видалення цифр і запис у TF10_2.txt ---
file_1_r = Open(file1_name, "r")
file_2_w = Open(file2_name, "w")

if file_1_r is not None and file_2_w is not None:
    text = file_1_r.read()
    # Видаляємо всі цифри
    text_no_digits = ''.join([ch for ch in text if not ch.isdigit()])

    # Запис по 10 символів у рядок
    for i in range(0, len(text_no_digits), 10):
        file_2_w.write(text_no_digits[i:i+10] + "\n")

    file_1_r.close()
    file_2_w.close()
    print("Файл TF10_2.txt сформовано!\n")

# --- в) читання TF10_2.txt і виведення ---
file_2_r = Open(file2_name, "r")
if file_2_r is not None:
    print("Вміст TF10_2.txt:")
    for line in file_2_r:
        print(line.strip())
    file_2_r.close()
