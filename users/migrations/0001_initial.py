# Generated by Django 4.2.5 on 2023-09-07 06:48

from django.db import migrations, models
import users.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Siteuser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, validators=[users.validators.validate_firstname_length], verbose_name='Имя')),
                ('lastname', models.CharField(max_length=100, validators=[users.validators.validate_lastname_length], verbose_name='Фамилия')),
                ('username', models.CharField(max_length=25, validators=[users.validators.validate_username_length, users.validators.validate_username_alphadigits], verbose_name='Имя пользователя')),
                ('password1', models.CharField(max_length=30, validators=[users.validators.validate_password_length, users.validators.validate_password_digit, users.validators.validate_password_uppercase])),
                ('password2', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('phone', models.CharField(max_length=15, validators=[users.validators.validate_phonenumber], verbose_name='Телефон')),
            ],
        ),
    ]