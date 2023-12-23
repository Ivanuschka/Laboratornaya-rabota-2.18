import argparse
import os


def add_student(students, surname, group_number, grades):
    """
    Добавить данные о студенте в список.
    """
    student = {
        'фамилия и инициалы': surname,
        'номер группы': group_number,
        'успеваемость': grades
    }
    students.append(student)
    # Сортировка по возрастанию номера группы
    students.sort(key=lambda x: x['номер группы'])
    return students


def display_students(students, min_average_grade):
    """
    Вывести фамилии и номера групп студентов с успеваемостью выше заданного значения.
    """
    found_students = [student for student in students if calculate_average_grade(student) > min_average_grade]

    if found_students:
        print("Студенты с успеваемостью выше {:.2f}:".format(min_average_grade))
        for student in found_students:
            print("Фамилия и инициалы: {}, Номер группы: {}".format(student['фамилия и инициалы'],
                                                                    student['номер группы']))
    else:
        print("Нет студентов с успеваемостью выше {:.2f}.".format(min_average_grade))


def calculate_average_grade(student):
    """
    Рассчитать средний балл студента.
    """
    grades = student['успеваемость']
    return sum(grades) / len(grades) if grades else 0.0


def main():
    parser = argparse.ArgumentParser(description='Управление списком студентов')
    parser.add_argument('--min-average-grade', type=float, default=4.0, help='Минимальный средний балл для вывода')
    parser.add_argument('--data-file', type=str, default=os.environ.get('STUDENTS_DATA_FILE', 'students_data.txt'),
                        help='Имя файла данных (по умолчанию: students_data.txt)')
    args = parser.parse_args()

    students = []
    while True:
        print("\n1. Добавить студента")
        print("2. Вывести студентов с успеваемостью выше {:.2f}".format(args.min_average_grade))
        print("3. Выйти")

        choice = input("Выберите действие (1/2/3): ")

        if choice == '1':
            surname = input("Введите фамилию и инициалы студента: ")
            group_number = input("Введите номер группы студента: ")
            grades = [float(input("Введите оценку {}-го предмета: ".format(i + 1))) for i in range(5)]
            students = add_student(students, surname, group_number, grades)
            print("Студент успешно добавлен!")
        elif choice == '2':
            display_students(students, args.min_average_grade)
        elif choice == '3':
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
