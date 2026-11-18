import django.utils.timezone
from django.db import migrations, models


def add_existing_emails(apps, schema_editor):
    Student = apps.get_model('students', 'Student')
    for student in Student.objects.filter(email__isnull=True):
        student.email = f"student-{student.pk}@ecole.sn"
        student.save(update_fields=['email'])

    Teacher = apps.get_model('students', 'Teacher')
    for teacher in Teacher.objects.filter(email__isnull=True):
        teacher.email = f"teacher-{teacher.pk}@ecole.sn"
        teacher.save(update_fields=['email'])


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_add_sample_roster'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='birth_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='created_at',
            field=models.DateTimeField(
                auto_now_add=True,
                default=django.utils.timezone.now,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='teacher',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True),
        ),
        migrations.RunPython(add_existing_emails, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
