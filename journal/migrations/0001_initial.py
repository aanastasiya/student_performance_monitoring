# Generated by Django 3.1.3 on 2020-11-24 08:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название кафедры')),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название дисциплины')),
                ('assessment', models.CharField(choices=[('CR', 'Зачет'), ('DF', 'Дифференцированный зачет'), ('EX', 'Экзамен')], default='CR', max_length=2)),
                ('hours', models.IntegerField(verbose_name='Академические часы')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.department')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=100, verbose_name='Отчество')),
                ('year', models.IntegerField(verbose_name='Курс')),
                ('faculty', models.CharField(max_length=200, verbose_name='Факультет')),
                ('specialty', models.CharField(max_length=200, verbose_name='Специальность')),
                ('group', models.CharField(max_length=50, verbose_name='Группа')),
                ('subject', models.ManyToManyField(to='journal.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('patronymic', models.CharField(max_length=100, verbose_name='Отчество')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.department')),
                ('subject', models.ManyToManyField(related_name='Дисциплина', to='journal.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(validators=[django.core.validators.MinValueValidator(2), django.core.validators.MaxValueValidator(5)], verbose_name='Оценка')),
                ('date', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='journal.subject')),
            ],
        ),
    ]