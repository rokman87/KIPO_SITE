from django.shortcuts import render
from .models import Groups, Subjects, Teachers, Cabinets, Schedules
from .forms import GroupsForm, SubjectsForm, TeachersForm, CabinetsForm, SchedulesForm
from users.models import Applications


def schedules(request, app_id):
    groups_db = Schedules.objects.filter(schedule_id=app_id)

    error = ''
    if request.method == 'POST':
        form = SchedulesForm(request.POST)
        if form.is_valid():
            applications_instance = Applications.objects.get(pk=app_id)
            form.instance.schedule_id=applications_instance
            form.save()
        else:
            error = 'Форма была неверной'

    form = SchedulesForm()

    data = {
        'form': form,
        'error': error,
        'app_id': app_id,
        'groups': groups_db,
    }
    return render(request, 'applications/schedules.html', data)


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


def groups(request, app_id):
    groups_db = Groups.objects.filter(schedule_id=app_id)

    error = ''
    if request.method == 'POST':
        form = GroupsForm(request.POST)
        if form.is_valid():
            applications_instance = Applications.objects.get(pk=app_id)
            form.instance.schedule_id = applications_instance
            form.save()
        else:
            error = 'Форма была неверной'

    form = GroupsForm()

    data = {
        'form': form,
        'error': error,
        'app_id': app_id,
        'groups': groups_db,
    }
    return render(request, 'applications/groups.html', data)


def subjects(request, app_id):
    groupsDB = Subjects.objects.filter(schedule_id=app_id)

    error = ''
    if request.method == 'POST':
        form = SubjectsForm(request.POST)
        if form.is_valid():
            applications_instance = Applications.objects.get(pk=app_id)
            form.instance.schedule_id = applications_instance
            form.save()
        else:
            error = 'Форма была неверной'

    form = SubjectsForm()

    data = {
        'form': form,
        'error': error,
        'app_id': app_id,
        'groups': groupsDB,
    }
    return render(request, 'applications/subjects.html', data)


def teachers(request, app_id):
    groups_db = Teachers.objects.filter(schedule_id=app_id)

    error = ''
    if request.method == 'POST':
        form = TeachersForm(request.POST)
        if form.is_valid():
            applications_instance = Applications.objects.get(pk=app_id)
            form.instance.schedule_id = applications_instance
            form.save()
        else:
            error = 'Форма была неверной'

    form = TeachersForm()

    data = {
        'form': form,
        'error': error,
        'app_id': app_id,
        'groups': groups_db,
    }
    return render(request, 'applications/teachers.html', data)


def cabinets(request, app_id):
    groups_db = Cabinets.objects.filter(schedule_id=app_id)

    error = ''
    if request.method == 'POST':
        form = CabinetsForm(request.POST)
        if form.is_valid():
            applications_instance = Applications.objects.get(pk=app_id)
            form.instance.schedule_id = applications_instance
            form.save()
        else:
            error = 'Форма была неверной'

    form = CabinetsForm()

    data = {
        'form': form,
        'error': error,
        'app_id': app_id,
        'groups': groups_db,
    }
    return render(request, 'applications/cabinets.html', data)


def types_lessons(request, app_id):
    return render(request, 'applications/types_lessons.html', {'app_id': app_id})


def publication(request, app_id):
    return render(request, 'applications/publication.html', {'app_id': app_id})


def settings(request, app_id):
    return render(request, 'applications/settings.html', {'app_id': app_id})
