def Open(file_name, mode):
    try:
        file = open(file_name, mode, encoding="utf-8")
    except:
        print("Файл", file_name, "не вдалося відкрити!")
        return None
    else:
        return file


file1_name = "TF10_1.txt"
file2_name = "TF10_2.txt"

# --- а) створення TF10_1.txt ---
file_1_w = Open(file1_name, "w")
if file_1_w:
    file_1_w.write("Python3 is great!\n")
    file_1_w.write("File123 processing test.\n")
    file_1_w.write("Numbers 9876543210 should be removed!\n")
    file_1_w.close()

# --- б) читання TF10_1.txt, видалення цифр і запис у TF10_2.txt ---
file_1_r = Open(file1_name, "r")
file_2_w = Open(file2_name, "w")

if file_1_r and file_2_w:
    text = file_1_r.read()
    # видаляємо цифри і символи переводу рядка
    text_no_digits = ''.join([ch for ch in text if not ch.isdigit() and ch != '\n'])

    # запис по 10 символів у рядок
    for i in range(0, len(text_no_digits), 10):
        file_2_w.write(text_no_digits[i:i+10] + "\n")

    file_1_r.close()
    file_2_w.close()

# --- в) читання TF10_2.txt і виведення ---
file_2_r = Open(file2_name, "r")
if file_2_r:
    print("Вміст TF10_2.txt:")
    for line in file_2_r:
        print(line.strip())
    file_2_r.close()
