# Generated by Django 4.2.5 on 2023-09-07 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_application'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='institution_type',
            field=models.CharField(max_length=30, verbose_name='Тип заведения'),
        ),
        migrations.AlterField(
            model_name='application',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='application',
            name='schedules',
            field=models.CharField(max_length=200, verbose_name='Расписаний'),
        ),
    ]
