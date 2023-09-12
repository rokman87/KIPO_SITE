from django.db import models
from .validators import (validate_firstname_length,
                         validate_lastname_length,
                         validate_username_length, validate_username_alphadigits,
                         validate_password_length, validate_password_digit,
                         validate_password_uppercase,
                         validate_phonenumber)


class Siteuser(models.Model):
    firstname = models.CharField(max_length=100, verbose_name='Имя', validators=[validate_firstname_length])
    lastname = models.CharField(max_length=100, verbose_name='Фамилия', validators=[validate_lastname_length])
    username = models.CharField(max_length=25, verbose_name='Имя пользователя',
                                validators=[validate_username_length, validate_username_alphadigits])
    password1 = models.CharField(max_length=30,
                                 validators=[validate_password_length, validate_password_digit,
                                             validate_password_uppercase])
    password2 = models.CharField(max_length=30)
    email = models.EmailField(verbose_name='Почта')
    phone = models.CharField(max_length=15, verbose_name='Телефон', validators=[validate_phonenumber])


class Applications(models.Model):
    name = models.CharField('Название', max_length=50)
    institution_type = models.CharField('Тип заведения', max_length=30)
    schedules = models.CharField('Расписаний', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Приложение'
        verbose_name_plural = 'Приложения'


