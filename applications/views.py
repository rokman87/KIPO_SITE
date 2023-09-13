from django.shortcuts import render
from .models import Groups, Subjects, Teachers, Cabinets, Schedules
from .forms import GroupsForm, SubjectsForm, TeachersForm, CabinetsForm, SchedulesForm
from users.models import Applications


# Общая функция для обработки форм и моделей
def handle_form(request, app_id, model_class, form_class, template_name):
    instances = model_class.objects.filter(schedule_id=app_id)
    error = ''

    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            applications_instance = Applications.objects.get(pk=app_id)
            form.instance.schedule_id = applications_instance
            form.save()
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


def schedules(request, app_id):
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
    return render(request, 'applications/bells.html', {'app_id': app_id})


def work_times(request, app_id):
    return render(request, 'applications/work_times.html', {'app_id': app_id})


def workloads(request, app_id):
    return render(request, 'applications/workloads.html', {'app_id': app_id})


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
