# Generated by Django 4.2.5 on 2023-09-19 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tasks',
            name='deadline',
            field=models.CharField(default='', max_length=50, verbose_name='Срок выполнения задачи'),
            preserve_default=False,
        ),
    ]
