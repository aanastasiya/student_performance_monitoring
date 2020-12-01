from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Student(models.Model):
    name = models.CharField('Имя', max_length=100)
    surname = models.CharField('Фамилия', max_length=100)
    patronymic = models.CharField('Отчество', max_length=100)
    year = models.IntegerField('Курс')
    faculty = models.CharField('Специальность', max_length=200)
    specialty = models.CharField('Факультет', max_length=200)
    group = models.CharField('Группа', max_length=50)
    subject = models.ManyToManyField('Subject', verbose_name='Дисциплина')

    def __str__(self):
        return f"{self.name} {self.patronymic} {self.surname}"

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'



class Grade(models.Model):
    student = models.ForeignKey('Student', verbose_name='Студент', on_delete=models.CASCADE)
    value = models.IntegerField('Балл', validators=[MinValueValidator(2), MaxValueValidator(5)])
    date = models.DateField('Дата', auto_now_add=True)
    subject = models.ForeignKey('Subject', verbose_name='Дисциплина', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.value}, {self.subject}, {self.student}, {self.date}'

    class Meta:
        verbose_name = 'Балл'
        verbose_name_plural = 'Баллы'
        ordering = ("student", "subject")


class Subject(models.Model):
    CREDIT = 'CR'
    DIFF_CREDIT = 'DF'
    EXAM = 'EX'
    ASSESSMENT_CHOICES = [
        (CREDIT, 'Зачет'),
        (DIFF_CREDIT, 'Дифференцированный зачет'),
        (EXAM, 'Экзамен'),
    ]

    title = models.CharField('Название дисциплины', max_length=200)
    assessment = models.CharField(verbose_name='Форма контроля',
                                  max_length=2,
                                  choices=ASSESSMENT_CHOICES,
                                  default=CREDIT)
    hours = models.IntegerField('Академические часы')
    department = models.ForeignKey('Department', verbose_name='Кафедра', on_delete=models.CASCADE)

    def __str__(self):
        def find_assessment(abbreviation):
            for assessment in self.ASSESSMENT_CHOICES:
                if abbreviation in assessment:
                    return assessment[1]

        return f'{self.title}'

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'


class Professor(models.Model):
    name = models.CharField('Имя', max_length=100)
    surname = models.CharField('Фамилия', max_length=100)
    patronymic = models.CharField('Отчество', max_length=100)
    department = models.ForeignKey('Department', verbose_name='Кафедра', on_delete=models.CASCADE)
    subject = models.ManyToManyField('Subject', verbose_name='Дисциплина')

    def __str__(self):
        return f'{self.name} {self.patronymic} {self.surname}, {self.department}'

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Department(models.Model):
    title = models.CharField('Название кафедры', max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'
