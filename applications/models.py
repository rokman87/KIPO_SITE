from django.db import models
from users.models import Applications


class Schedules(models.Model):
    title = models.CharField('Название', max_length=50)
    week_date = models.DateField('Дата')
    week_days = models.CharField('Дни недели', max_length=50)
    lessons_counts = models.CharField('Уроков в день', max_length=50)
    week_type = models.CharField('Тип недели', max_length=50)
    schedule_id = models.ForeignKey(Applications, on_delete=models.CASCADE, related_name='schedules_applications')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'


class WorkLoads(models.Model):
    name = models.CharField('Предмет', max_length=50)
    group = models.CharField('Группа', max_length=50)
    teacher = models.CharField('Преподаватель', max_length=50)
    cabinet = models.CharField('Аудитория', max_length=50)
    lessons = models.CharField('Уроков', max_length=50)
    schedule_id = models.ForeignKey(Applications, on_delete=models.CASCADE, related_name='WorkLoads')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Нагрузка'
        verbose_name_plural = 'Нагрузки'


class Groups(models.Model):
    title = models.CharField('Название', max_length=50)
    abbreviation = models.CharField('Сокращение', max_length=50)
    students_count = models.CharField('Количество учащихся', max_length=50)
    cabinets = models.CharField('Аудитории', max_length=50)
    color = models.CharField('Цвет', max_length=50)
    schedule_id = models.ForeignKey(Applications, on_delete=models.CASCADE, related_name='Groups')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Subjects(models.Model):
    title = models.CharField('Название', max_length=50)
    abbreviation = models.CharField('Сокращение', max_length=50)
    cabinets = models.CharField('Аудитории', max_length=50)
    color = models.CharField('Цвет', max_length=50)
    schedule_id = models.ForeignKey(Applications, on_delete=models.CASCADE, related_name='Subjects')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Cabinets(models.Model):
    title = models.CharField('Название', max_length=50)
    abbreviation = models.CharField('Сокращение', max_length=50)
    seat_number = models.CharField('Количество мест', max_length=50)
    building = models.CharField('Корпус', max_length=50)
    color = models.CharField('Цвет', max_length=50)
    schedule_id = models.ForeignKey(Applications, on_delete=models.CASCADE, related_name='Cabinets')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Аудитория'
        verbose_name_plural = 'Аудитории'


class Teachers(models.Model):
    name = models.CharField('Преподаватель', max_length=50)
    abbreviation = models.CharField('Сокращение', max_length=50)
    position = models.CharField('Должность', max_length=50)
    subjects = models.ManyToManyField(Subjects)
    cabinets = models.ManyToManyField(Cabinets)
    color = models.CharField('Цвет', max_length=50)
    schedule_id = models.ForeignKey(Applications, on_delete=models.CASCADE, related_name='Teachers')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
