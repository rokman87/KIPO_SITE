# Generated by Django 4.2.5 on 2023-09-07 11:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_rename_applications_applicationss'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Applicationss',
            new_name='Applications',
        ),
    ]
