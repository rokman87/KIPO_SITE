# Generated by Django 4.2.5 on 2023-09-14 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0003_alter_workloads_lessons_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cabinets',
            name='seat_number',
            field=models.PositiveIntegerField(verbose_name='Количество мест'),
        ),
    ]
