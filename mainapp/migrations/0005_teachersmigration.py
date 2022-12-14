# Generated by Django 3.2 on 2022-08-31 11:35

from django.db import migrations
from random import randrange, choice

def forwards_func_teachers(apps, schema_editor):
    Сorses = apps.get_model("mainapp", "Courses")
    corses_id = [i.pk for i in Сorses.objects.all()]

    # Get model
    CourseTeachers = apps.get_model("mainapp", "CourseTeachers")
    # Create model's objects
    for i in range(8):
        new_teacher = CourseTeachers.objects.create(
                        name_first=f'Преподаватель{i}',
                        name_second='Иванов',
                        day_birth="2022-08-31",
                    )
        new_teacher.course.add(Сorses.objects.get(pk=choice(corses_id)))
        new_teacher.course.add(Сorses.objects.get(pk=choice(corses_id)))


def reverse_func_teachers(apps, schema_editor):
    # Get model
    teachers = apps.get_model("mainapp", "CourseTeachers")
    # Delete objects
    teachers.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [('mainapp', '0004_lessonsmigration')]

    operations = [migrations.RunPython(forwards_func_teachers, reverse_func_teachers)]
