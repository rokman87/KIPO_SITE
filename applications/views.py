from django.shortcuts import render, redirect
from .models import Groups, Subjects, Teachers, Cabinets, Schedules, Bells, WorkLoads
from .forms import GroupsForm, SubjectsForm, TeachersForm, CabinetsForm, SchedulesForm, WorkLoadsForm
from users.models import Applications
from datetime import datetime, timedelta


# Общая функция для обработки форм и моделей
def handle_form(request, app_id, model_class, form_class, template_name):
    instances = model_class.objects.filter(application_id=app_id)
    error = ''

    if request.method == 'POST':
        if 'action' in request.POST and request.POST['action'] == 'ins':
            form = form_class(request.POST)
            if form.is_valid():
                applications_instance = Applications.objects.get(pk=app_id)
                form.instance.application_id = applications_instance

                # Сохранение объект Schedule в базе данных
                schedule = form.save()

                if model_class == Schedules:
                    # Получение id созданного объекта
                    scheb_id = schedule.id
                    # Вызов функции bells_create с передачей scheb_id
                    bells_create(request, scheb_id)
            else:
                error = 'Форма была неверной'
    else:
        form = form_class()

    data = {
        'form': form,
        'error': error,
        'app_id': app_id,
        'groups': instances,
    }

    return render(request, template_name, data)


# Общая функция для обработки форм и моделей
# Общая функция для обработки форм и моделей
def handle_form_schedule(request, app_id, model_class, form_class, template_name):
    instances = model_class.objects.filter(schedule_id__application_id=app_id)
    error = ''

    if request.method == 'POST':
        if 'action' in request.POST and request.POST['action'] == 'ins':
            form = form_class(request.POST)
            if form.is_valid():
                applications_instance = Applications.objects.get(pk=app_id)
                form.instance.schedule_id.application_id = applications_instance

                # Сохранение объекта в базе данных
                form.save()

                if model_class == Schedules:
                    # Получение id созданного объекта
                    scheb_id = form.instance.id
                    # Вызов функции bells_create с передачей scheb_id
                    bells_create(request, scheb_id)
            else:
                error = 'Форма была неверной'
    else:
        form = form_class()

    data = {
        'form': form,
        'error': error,
        'app_id': app_id,
        'groups': instances,
    }

    return render(request, template_name, data)


def bells_create(request, scheb_id):
    # Получаем объект Schedules по его id
    schedule = Schedules.objects.get(id=scheb_id)

    # Получаем значение поля lessons_counts
    lessons_counts = schedule.lessons_counts
    lessons_counts_int = int(lessons_counts)

    # Создаем список дней недели, которые у вас есть (предположим, что это понедельник, вторник, среда и так далее)
    days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]

    # Проходимся по каждому дню недели и каждому уроку и создаем объекты Bells
    for day in days_of_week:
        # Определяем начальное время (предположим, что первый урок начинается в 08:00)
        start_time = datetime.strptime("08:00", "%H:%M")
        for lesson_number in range(1, lessons_counts_int + 1):
            lesson_number_str = str(lesson_number)
            lesson = f"Урок {lesson_number_str}"

            # Вычисляем время начала и конца урока на основе номера урока
            time_start = start_time.strftime("%H:%M")
            time_end = (start_time + timedelta(minutes=80)).strftime("%H:%M")

            bell = Bells(
                lesson=lesson,
                time_start=time_start,
                time_end=time_end,
                week_day=day,
                type="Обычный",
                schedule_id=schedule  # Используйте экземпляр Schedules вместо его ID
            )
            bell.save()  # Сохраняем объект в базе данных

            # Увеличиваем время начала для следующего урока, учитывая перерыв в 10 минут
            start_time += timedelta(minutes=80 + 10)


def delete_schedule(request, app_id, element_id, table, elem):
    if request.method == 'POST':
        if element_id:
            # Удаление элемента из таблицы schedules
            table.objects.filter(id=element_id).delete()
    return redirect(f'/applications/{app_id}/{elem}')


# Измените функцию schedules
def schedules(request, app_id):
    if request.method == 'POST':
        if 'action' in request.POST and request.POST['action'] == 'del':
            element_id = request.POST.get('element_id')
            return delete_schedule(request, app_id, element_id, Schedules, "schedules")

    return handle_form(request, app_id, Schedules, SchedulesForm, 'applications/schedules.html')


def groups(request, app_id):
    return handle_form(request, app_id, Groups, GroupsForm, 'applications/groups.html')


def subjects(request, app_id):
    return handle_form(request, app_id, Subjects, SubjectsForm, 'applications/subjects.html')


def teachers(request, app_id):
    return handle_form(request, app_id, Teachers, TeachersForm, 'applications/teachers.html')


def cabinets(request, app_id):
    return handle_form(request, app_id, Cabinets, CabinetsForm, 'applications/cabinets.html')


def bells(request, app_id):
    selected_day = request.GET.get('day')  # Получаем выбранный день из строки запроса
    if selected_day == None:
        selected_day = 'Понедельник'

    if selected_day:
        bells = Bells.objects.filter(schedule_id__application_id=app_id, week_day=selected_day)
    else:
        bells = Bells.objects.filter(schedule_id__application_id=app_id)

    data = {
        'bells': bells,
        'selected_day': selected_day,
        'app_id': app_id,
    }

    return render(request, 'applications/bells.html', data)


def work_times(request, app_id):
    return render(request, 'applications/work_times.html', {'app_id': app_id})


def workloads(request, app_id):
    return handle_form_schedule(request, app_id, WorkLoads, WorkLoadsForm, 'applications/workloads.html')


def lessons(request, app_id):
    return render(request, 'applications/lessons.html', {'app_id': app_id})


def printSchedule(request, app_id):
    return render(request, 'applications/printSchedule.html', {'app_id': app_id})


def types_lessons(request, app_id):
    return render(request, 'applications/types_lessons.html', {'app_id': app_id})


def publication(request, app_id):
    return render(request, 'applications/publication.html', {'app_id': app_id})


def settings(request, app_id):
    return render(request, 'applications/settings.html', {'app_id': app_id})
