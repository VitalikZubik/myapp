# Generated by Django 4.2.5 on 2023-09-23 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_tasks_deadline'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tasks',
            old_name='task_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='tasks',
            old_name='task_name',
            new_name='name',
        ),
    ]
