# Generated by Django 4.2.5 on 2023-09-07 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_application_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Application',
            new_name='Applications',
        ),
    ]