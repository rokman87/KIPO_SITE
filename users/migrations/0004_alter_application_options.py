# Generated by Django 4.2.5 on 2023-09-07 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_application_institution_type_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'verbose_name': 'Приложение', 'verbose_name_plural': 'Приложения'},
        ),
    ]
