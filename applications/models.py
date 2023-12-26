from django.db import models
from users.models import Applications
from django.utils import timezone


class Schedules(models.Model):
    title = models.CharField('Название', max_length=50)
    week_date = models.DateField('Дата')
    week_days = models.ManyToManyField('WeekDay')
    lessons_counts = models.CharField('Уроков в день', max_length=50)
    week_type = models.CharField('Тип недели', max_length=50)
    application_id = models.ForeignKey(Applications, on_delete=models.CASCADE, related_name='schedules_applications')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписания'


class WeekDay(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'День недели'
        verbose_name_plural = 'Дни недели'


class Groups(models.Model):
    title = models.CharField('Название', max_length=50)
    abbreviation = models.CharField('Сокращение', max_length=50)
    students_count = models.CharField('Количество учащихся', max_length=50)
    cabinets = models.CharField('Аудитории', max_length=50)
    color = models.CharField('Цвет', max_length=50)
    application_id = models.ForeignKey(Applications, on_delete=models.CASCADE, related_name='Groups')

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
    application_id = models.ForeignKey(Applications, on_delete=models.CASCADE, related_name='Subjects')

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
    application_id = models.ForeignKey(Applications, on_delete=models.CASCADE, related_name='Cabinets')

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
    application_id = models.ForeignKey(Applications, on_delete=models.CASCADE, related_name='Teachers')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Bells(models.Model):
    lesson = models.CharField('Урок', max_length=50)
    time_start = models.TimeField('Начало урока', default=timezone.now)
    time_end = models.TimeField('Конец урока', default=timezone.now)
    week_day = models.CharField('День недели', max_length=50)
    type = models.CharField('Тип', max_length=50)
    schedule_id = models.ForeignKey(Schedules, on_delete=models.CASCADE, related_name='Bells')

    def __str__(self):
        return f'{self.schedule_id} - {self.week_day} - {self.lesson}'

    class Meta:
        verbose_name = 'Звонок'
        verbose_name_plural = 'Звонки'


class WorkLoads(models.Model):
    subjects = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    groups = models.ManyToManyField(Groups)
    teachers = models.ManyToManyField(Teachers)
    cabinets = models.ManyToManyField(Cabinets)
    lessons_count = models.PositiveIntegerField(default=0)
    schedule_id = models.ForeignKey(Schedules, on_delete=models.CASCADE, related_name='workloads')

    def __str__(self):
        return f'ID: {self.id} - Предмет: {self.subjects} - Группы: {", ".join(str(group) for group in self.groups.all())} - Преподаватели: {", ".join(str(teacher) for teacher in self.teachers.all())}'

    class Meta:
        verbose_name = 'Нагрузка'
        verbose_name_plural = 'Нагрузки'


class LessonsCells(models.Model):
    text = models.CharField('Текст', max_length=50)
    dataElementId = models.ManyToManyField(WorkLoads)
    cellName = models.CharField('Место', max_length=50)
    group = models.CharField('Группа', max_length=50)
    def __str__(self):
        return f'ID: {self.id} - Предмет: {self.text}'

    class Meta:
        verbose_name = 'Сетка уроков'
        verbose_name_plural = 'Сетки уроков'