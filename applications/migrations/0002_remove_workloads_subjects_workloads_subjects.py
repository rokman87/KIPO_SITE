# Generated by Django 4.2.5 on 2023-09-19 12:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('applications', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workloads',
            name='subjects',
        ),
        migrations.AddField(
            model_name='workloads',
            name='subjects',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='applications.subjects'),
            preserve_default=False,
        ),
    ]