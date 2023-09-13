# Generated by Django 4.2.5 on 2023-09-13 07:14

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0004_schedules'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cabinets',
            old_name='schedule_id',
            new_name='application_id',
        ),
        migrations.RenameField(
            model_name='groups',
            old_name='schedule_id',
            new_name='application_id',
        ),
        migrations.RenameField(
            model_name='schedules',
            old_name='schedule_id',
            new_name='application_id',
        ),
        migrations.RenameField(
            model_name='subjects',
            old_name='schedule_id',
            new_name='application_id',
        ),
        migrations.RenameField(
            model_name='teachers',
            old_name='schedule_id',
            new_name='application_id',
        ),
        migrations.RenameField(
            model_name='workloads',
            old_name='schedule_id',
            new_name='application_id',
        ),
        migrations.CreateModel(
            name='Bells',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lesson', models.CharField(max_length=50, verbose_name='Урок')),
                ('time_start', models.TimeField(default=django.utils.timezone.now, verbose_name='Начало урока')),
                ('time_end', models.TimeField(default=django.utils.timezone.now, verbose_name='Конец урока')),
                ('week_day', models.CharField(max_length=50, verbose_name='День недели')),
                ('type', models.CharField(max_length=50, verbose_name='Тип')),
                ('schedule_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Bells', to='applications.schedules')),
            ],
            options={
                'verbose_name': 'Звонок',
                'verbose_name_plural': 'Звонки',
            },
        ),
    ]
