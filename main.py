import django_setup
from education.models import Subject, Teacher, Class, Student


def add_subject():
    title = input("Введи назву предмету: ")
    description = input("Введи опис предмету: ")
    if Subject.objects.filter(title=title).exists():
        print("Такий предмет вже існує")
        return
    Subject.objects.create(
        title=title,
        description=description
        )
    print("Предмет успішно доданий")
    return

def add_teacher():
    first_name = input("Введіть ім'я вчителя: ")
    last_name = input("Введіть прізвище вчителя: ")
    email = input("Введать пошту вчителя: ")
    subjects = input("Введать предмети які викладає вчитель через кому: ").split(",")
    experience = int(input("Введіть трудовий стаж (років): "))

    teacher = Teacher.objects.create(
        first_name=first_name,
        last_name=last_name,
        email=email,
        experience=experience
    )

    for subject in subjects:
        sub = Subject.objects.filter(title=subject)
        if sub:
            teacher.subject.add(Subject.objects.get(title=subject))
        else:
            print(f"Предмата {subject} не існує, не додано до БД!")

    teacher.save()

def add_class():
    pass

def add_student():
    pass

def show_students_by_class():
    pass

def show_subjects_by_teacher():
    pass



while True:
    print("1 - додати предмет")
    print("2 - додати вчителя")
    print("3 - додати клас")
    print("4 - додати учня")
    print("5 - поазати всіх учнів класу")
    print("6 - показати всі предмети які викладає вчитель")
    print("7 - вихід")

    action = int(input(""))

    if action == 1:
        add_subject()
    if action == 2:
        add_teacher()
    if action == 3:
        add_class()
    if action == 4:
        add_student()
    if action == 5:
        show_students_by_class()
    if action == 6:
        show_subjects_by_teacher()
    if action == 7:
        break

