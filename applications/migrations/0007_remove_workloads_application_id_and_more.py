# Generated by Django 4.2.5 on 2023-09-14 08:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0006_weekday_remove_schedules_week_days_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workloads',
            name='application_id',
        ),
        migrations.RemoveField(
            model_name='workloads',
            name='cabinet',
        ),
        migrations.RemoveField(
            model_name='workloads',
            name='group',
        ),
        migrations.RemoveField(
            model_name='workloads',
            name='lessons',
        ),
        migrations.RemoveField(
            model_name='workloads',
            name='name',
        ),
        migrations.RemoveField(
            model_name='workloads',
            name='teacher',
        ),
        migrations.AddField(
            model_name='workloads',
            name='cabinets',
            field=models.ManyToManyField(to='applications.cabinets'),
        ),
        migrations.AddField(
            model_name='workloads',
            name='groups',
            field=models.ManyToManyField(to='applications.groups'),
        ),
        migrations.AddField(
            model_name='workloads',
            name='lessons_count',
            field=models.PositiveIntegerField(default=111),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workloads',
            name='schedule_id',
            field=models.ForeignKey(default=111, on_delete=django.db.models.deletion.CASCADE, related_name='workloads', to='applications.schedules'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workloads',
            name='subjects',
            field=models.ManyToManyField(to='applications.subjects'),
        ),
        migrations.AddField(
            model_name='workloads',
            name='teachers',
            field=models.ManyToManyField(to='applications.teachers'),
        ),
    ]