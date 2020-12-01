import mysql.connector
import json
import random
from datetime import date


# Данные
with open('names.json', 'r') as file:
    names = json.load(file)['names']

with open('surnames.json', 'r') as file:
    surnames = json.load(file)['surnames']

with open('patronymic.json', 'r') as file:
    patronymics = json.load(file)['patronymic']

with open('departments.json', 'r') as file:
    departments = json.load(file)['departments']

faculties = ['Политология', 'Бизнес-информатика', 'Прикладная информатика',
             'Технология продукции и организация общественного питания',
             'Торговое дело', 'Экономическая безопасность', 'Юриспруденция',
             'Технологические машины и оборудование', 'Информационная безопасность',
             'Социология', 'Туризм', 'Математическое обеспечение и администрирование информационных систем',
             'Прикладная математика и информатика', 'Государственное и муниципальное управление',
             'Лингвистика', 'Реклама и связи с общественностью', 'Дизайн', 'Экономика',
             'Психология', 'Товароведение', 'Управление персоналом', 'Таможенное дело',
             'Гостиничное дело', 'Менеджмент']

specialties = ['институт цифровой экономики и информационных технологий',
               'факультет "Международная школа бизнеса и мировой экономики"',
               'факультет "Экономики и права"',
               'факультет бизнеса "КАПИТАНЫ"',
               'факультет гостинично-ресторанной, туристической и спортивной индустрии',
               'факультет дистанционного обучения',
               'факультет маркетинга',
               'факультет менеджмента',
               'факультет экономики торговли и товароведения',
               'финансовый факультет']

subjects = ['безопасность жизнедеятельности', 'история', 'правоведение', 'русский язык и культура речи', 'психология',
            'социология', 'философия', 'математический анализ', 'линейная алгебра', 'аналитическая геометрия',
            'дискретная математика', 'функциональный анализ', 'базы данных', 'дифференциальные уравнения',
            'иностранный язык', 'интернет-программирование', 'операционные системы', 'системное программирование',
            'теория вероятностей и математическая статистика', 'физика', 'физическая культура'
            ]

# Запрос для добавления данных в бд
add_student = ("INSERT INTO `journal_student` (`name`, `surname`, `patronymic`, `year`, `faculty`, `specialty`, `group`) VALUES ")

add_subject = ("INSERT INTO `journal_subject` (`title`, `assessment`, `hours`, `department_id`) VALUES ")

add_professor = ("INSERT INTO `journal_professor` (`name`, `surname`, `patronymic`, `department_id`) VALUES ")

add_grade = ("INSERT INTO `journal_grade` (`value`, `date`, `student_id`, `subject_id`) VALUES ")

add_department = ("INSERT INTO `journal_department` (`title`, ) VALUES ")

add_professor_subject = ("INSERT INTO `journal_professor_subject` (`professor_id`, `subject_id`) VALUES ")

add_student_subject = ("INSERT INTO `journal_student_subject` (`student_id`, `subject_id`) VALUES ")


with open('queries.sql', 'a') as f:
    for department in departments:
        add_department += f"('{department}'),"
    add_department = add_department[:-1]
    f.write(add_department + ';\n')

    assessment = ['CR', 'DF', 'EX']
    for subject in subjects:
        add_subject += f"('{subject}','{assessment[random.randint(0, 2)]}',{random.randint(300, 500)}," \
                       f"{random.randint(1, len(departments))}),"
    add_subject = add_subject[:-1]
    f.write(add_subject + ';\n')

    for i in range(0, 20000):
        add_student += f"('{names[random.randint(0, len(names) - 1)]}'," \
                       f"'{surnames[random.randint(0, len(surnames) - 1)]}'," \
                       f"'{patronymics[random.randint(0, len(patronymics) - 1)]}',{random.randint(1, 5)}," \
                       f"'{faculties[random.randint(0, len(faculties) - 1)]}'," \
                       f"'{specialties[random.randint(0, len(specialties) - 1)]}',{random.randrange(200, 500, 10)}),"
        for j in range(0, 50):
            add_grade += f"({random.randint(2, 5)},'{date(2020, random.randint(1, 12), random.randint(1, 28))}'," \
                         f"{i + 1},{random.randint(1, len(subjects))}),"
    add_student = add_student[:-1]
    add_grade = add_grade[:-1]
    f.write(add_student + ';\n')
    f.write(add_grade + ';\n')

    for i in range(0, 30):
        add_professor += f"('{names[random.randint(0, len(names) - 1)]}'," \
                         f"'{surnames[random.randint(0, len(surnames) - 1)]}'," \
                         f"'{patronymics[random.randint(0, len(patronymics) - 1)]}'," \
                         f"{random.randint(1, len(departments))}),"
    add_professor = add_professor[:-1]
    f.write(add_professor + ';\n')

    for i in range(1, 31):
        professor_subjects = random.sample(range(1, len(subjects) + 1), 5)
        for j in range(0, 5):
            add_professor_subject += f"({i},{professor_subjects[j]}),"
    add_professor_subject = add_professor_subject[:-1]
    f.write(add_professor_subject + ';\n')

    for i in range(1, 20001):
        student_subjects = random.sample(range(1, len(subjects) + 1), 5)
        for j in range(0, 5):
            add_student_subject += f"({i},{student_subjects[j]}),"
    add_student_subject = add_student_subject[:-1]
    f.write(add_student_subject + ';\n')
