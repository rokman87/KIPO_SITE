# Generated by Django 4.2.5 on 2023-09-07 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_rename_applicationss_applications'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Applications',
            new_name='Application',
        ),
    ]
