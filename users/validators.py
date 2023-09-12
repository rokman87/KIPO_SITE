from django.core.exceptions import ValidationError
import re

def validate_firstname_length(value):
    length= len(value)
    if length < 2:
        raise ValidationError("Длина имени должна составлять не менее 2 символов")
    else:
        return value

def validate_lastname_length(value):
    length= len(value)
    if length < 2:
        raise ValidationError("Длина фамилии должна составлять не менее 2 символов")
    else:
        return value

def validate_username_length(value):
    length= len(value)
    if length < 3 or length > 25:
        raise ValidationError("Длина имени пользователя должна составлять от 3 до 25 символов")
    else:
        return value


def validate_username_alphadigits(value):
    validmatch= re.match('^[\w]+$', value)
    if not validmatch:
        raise ValidationError("Имя пользователя может содержать только алфавитные символы и цифры")
    else:
        return value

def validate_password_length(value):
    length= len(value)
    if length < 8 or length > 30:
        raise ValidationError("Длина пароля должна составлять не менее 8 символов и не более 30 символов")
    else:
        return value

def validate_password_digit(value):
    if not re.search(r"[\d]+", value):
        raise ValidationError("Пароль должен содержать по крайней мере одну цифру")
    else:
        return value

def validate_password_uppercase(value):
    if not re.search(r"[A-Z]+", value):
        raise ValidationError("Пароль должен содержать по крайней мере один символ верхнего регистра")
    else:
        return value


def validate_phonenumber(value):
    regex= r"\(\w{3}\)\w{3}-\w{4}"
    regex2= r"\w{3}-\w{3}-\w{4}"
    regex3= r"\b\w{10,11}\b"
    if not re.search(regex, value) and not re.search(regex2, value) and not re.search(regex3, value):
        raise ValidationError("Номер телефона должен быть формата (###)###-###, ###-###-###, ##########, or ########### ")
    else:
        return value
