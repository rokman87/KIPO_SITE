# Generated by Django 4.2.5 on 2023-09-12 12:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_delete_schedules'),
        ('applications', '0003_delete_schedules'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Название')),
                ('week_date', models.DateField(verbose_name='Дата')),
                ('week_days', models.CharField(max_length=50, verbose_name='Дни недели')),
                ('lessons_counts', models.CharField(max_length=50, verbose_name='Уроков в день')),
                ('week_type', models.CharField(max_length=50, verbose_name='Тип недели')),
                ('schedule_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules_applications', to='users.applications')),
            ],
            options={
                'verbose_name': 'Расписание',
                'verbose_name_plural': 'Расписания',
            },
        ),
    ]