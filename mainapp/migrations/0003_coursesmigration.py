from django.db import migrations


def forwards_func_courses(apps, schema_editor):
    # Get model
    Courses = apps.get_model("mainapp", "Courses")
    # Create model's objects
    for i in range(8):
        Courses.objects.create(
            name=f'Курс №{i}',
            cost=1000,
            cover=f'img/course{i:03}.jpg',
            description="Python предназначен для разработки и изучения новых приложений. \
                Мы предлагаем непросто изучить новый язык программирования, но и научиться применять его на практике. \
                Этот курс полезен не только тем, кто хочет научиться программировать, но и всем тем, кому не хватает \
                времени на выполнение практических заданий, а также тем, у кого нет возможности посещать курсы. \
                Курс состоит из 7 встреч — одно занятие в неделю длительностью 3 часа.\r\nВстречи \
                проводятся по воскресеньям с 14:00.",
        )


def reverse_func_courses(apps, schema_editor):
    # Get model
    Courses = apps.get_model("mainapp", "Courses")
    # Delete objects
    Courses.objects.all().delete()


class Migration(migrations.Migration):
    dependencies = [("mainapp", "0002_data_migration")]
    operations = [migrations.RunPython(forwards_func_courses, reverse_func_courses)]
