from django.shortcuts import render, redirect
from .models import Groups, Subjects, Teachers, Cabinets, Schedules, Bells, WorkLoads
from .forms import GroupsForm, SubjectsForm, TeachersForm, CabinetsForm, SchedulesForm, BellForm, WorkLoadsForm
from users.models import Applications
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.http import HttpResponseRedirect


# Общая функция для обработки форм и моделей
def handle_form(request, app_id, model_class, form_class, template_name):
    week_title = find_week_title(request)
    instances = model_class.objects.filter(application_id=app_id)
    error = ''

    if request.method == 'POST':
        if 'action' in request.POST and request.POST['action'] == 'ins':
            form = form_class(request.POST)
            if form.is_valid():
                applications_instance = Applications.objects.get(pk=app_id)
                form.instance.application_id = applications_instance
                form.save()
                if model_class == Schedules:
                    # Сохранение объект Schedule в базе данных
                    schedule = form.save()

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
        'title': week_title
    }

    return render(request, template_name, data)


def handle_form_sched(request, app_id, model_class, form_class, template_name, sched_id):
    week_title = find_week_title(request)
    instances = model_class.objects.filter(schedule_id=sched_id)
    error = ''
    field_errors = {}

    if request.method == 'POST':
        if 'action' in request.POST and request.POST['action'] == 'ins':
            form = form_class(request.POST)
            if form.is_valid():
                schedules_instance = Schedules.objects.get(pk=sched_id)
                form.instance.schedule_id = schedules_instance
                form.save()
            else:
                # Ошибки в форме, можно их получить и передать в контекст
                errors = form.errors.as_data()
                # Остальной код для обработки ошибок
                error = 'Форма содержит ошибки. Пожалуйста, проверьте поля формы.'
                # Дополнительно можно добавить вывод ошибок для каждого поля

                for field, error_list in errors.items():
                    field_errors[field] = [str(error) for error in error_list]
    else:
        form = form_class()

    data = {
        'form': form,
        'error': error,
        'app_id': app_id,
        'groups': instances,
        'title': week_title,
        'field_errors': field_errors  # Добавьте это в контекст
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
            time_end = (start_time + timedelta(minutes=90)).strftime("%H:%M")

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
            start_time += timedelta(minutes=90 + 10)


def delete_schedule(request, app_id, element_id, table, elem):
    if request.method == 'POST':
        if element_id:
            # Удаление элемента из таблицы schedules
            table.objects.filter(id=element_id).delete()

            # Очистить куки 'selectedElementId'
            response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            response.delete_cookie('selectedElementId')
            return response
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
    week_title = find_week_title(request)
    sched_id = request.COOKIES.get('selectedElementId')
    if selected_day == None:
        selected_day = 'Понедельник'

    if selected_day:

        bells = Bells.objects.filter(schedule_id=sched_id, week_day=selected_day)
    else:
        bells = Bells.objects.filter(schedule_id=sched_id)

    data = {
        'bells': bells,
        'selected_day': selected_day,
        'app_id': app_id,
        'title': week_title
    }

    return render(request, 'applications/bells.html', data)


def edit_bells(request):
    bells = Bell.objects.all()
    form = BellForm()

    if request.method == 'POST':
        form = BellForm(request.POST)
        if form.is_valid():
            # Обработка формы и сохранение данных в базу данных
            time_start = form.cleaned_data['time_start']
            time_end = form.cleaned_data['time_end']
            # Далее обновите соответствующий объект Bell в базе данных

    data = {
        'bells': bells,
        'form': form
    }

    return render(request, 'edit_bells.html', data)


def work_times(request, app_id):
    return render(request, 'applications/work_times.html', {'app_id': app_id})


def workloads(request, app_id):
    sched_id = request.COOKIES.get('selectedElementId')
    return handle_form_sched(request, app_id, WorkLoads, WorkLoadsForm, 'applications/workloads.html', sched_id)


def lessons(request, app_id):
    week_title = find_week_title(request)
    sched_id = request.COOKIES.get('selectedElementId')
    try:
        sched = Schedules.objects.get(id=sched_id)
        lessons_counts = int(sched.lessons_counts)
        lesson_numbers = list(range(1, lessons_counts + 1))
        lessons_days = sched.week_days.all()
        lessons_days_counts = len(lessons_days)
        lessons_days_number = list(range(1, lessons_days_counts + 1))

    except Schedules.DoesNotExist:
        lesson_numbers = 0

    groups = Groups.objects.all()
    groups_filter = groups.filter(application_id=app_id)

    instances = WorkLoads.objects.filter(schedule_id=sched_id)

    data = {
        'app_id': app_id,
        'title': week_title,
        'sched': sched,
        'lesson_numbers': lesson_numbers,
        'lessons_days_number': lessons_days_number,
        'groups': groups_filter,
        'instances': instances,
    }

    return render(request, 'applications/lessons.html', data)


def printSchedule(request, app_id):
    week_title = find_week_title(request)
    data = {
        'app_id': app_id,
        'title': week_title
    }
    return render(request, 'applications/printSchedule.html', data)


def types_lessons(request, app_id):
    return render(request, 'applications/types_lessons.html', {'app_id': app_id})


def publication(request, app_id):
    return render(request, 'applications/publication.html', {'app_id': app_id})


def settings(request, app_id):
    return render(request, 'applications/settings.html', {'app_id': app_id})


def find_week_title(request):
    week_title = None
    if request.COOKIES.get('selectedElementId'):
        sched_id = request.COOKIES.get('selectedElementId')
        sched_instance = Schedules.objects.get(id=sched_id)
        week_title = sched_instance.title
    else:
        week_title = 'Не выбрано!'
    return week_title


def clear_cookie(request):
    response.delete_cookie('selectedElementId')
