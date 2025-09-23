# Робота з файлами. Перший студент
# Створює текстовий файл і записує у нього своє прізвище та питання для другого студента

def open_file(file_name, mode):
    """Функція для відкриття файлу з обробкою виключень"""
    try:
        file = open(file_name, mode, encoding="utf-8")
    except Exception as e:
        print("Помилка відкриття файлу:", e)
        return None
    else:
        return file


# Назва файлу, з яким працюватимуть усі студенти
file_name = "students_questions.txt"

# Створення і запис даних у файл
file = open_file(file_name, "w")
if file:
    try:
        # Прізвище та питання
        file.write("Прізвище: Козловський\n")
        file.write("Питання: Як у Python прочитати вміст текстового файлу та вивести його на екран?\n")
        print(f"Дані успішно записані у файл {file_name}")
    except Exception as e:
        print("Помилка запису у файл:", e)
    finally:
        file.close()
