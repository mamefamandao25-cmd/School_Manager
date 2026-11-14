from django.db import migrations


def add_sample_roster(apps, schema_editor):
    Student = apps.get_model('students', 'Student')
    Teacher = apps.get_model('students', 'Teacher')

    students = [
        ('Aissatou', 'Diop', 'L1'),
        ('Moussa', 'Ba', 'L2'),
        ('Mariama', 'Fall', 'L3'),
        ('Ibrahima', 'Kane', 'L1'),
    ]
    for first_name, last_name, classe in students:
        Student.objects.get_or_create(
            first_name=first_name,
            last_name=last_name,
            classe=classe,
            defaults={'active': True},
        )

    teachers = [
        ('Awa', 'Diop', 'Sciences'),
        ('Ousmane', 'Ba', 'Histoire-Géographie'),
    ]
    for first_name, last_name, subject in teachers:
        Teacher.objects.get_or_create(
            first_name=first_name,
            last_name=last_name,
            subject=subject,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_sample_roster, migrations.RunPython.noop),
    ]
