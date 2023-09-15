from .models import Groups, Subjects, Teachers, Cabinets, Schedules, Bells, WorkLoads
from django.forms import ModelForm, TextInput, DateInput, SelectMultiple
from django import forms


class GroupsForm(ModelForm):
    class Meta:
        model = Groups
        fields = ['title', 'abbreviation', 'students_count', 'color']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название группы'
            }),
            "abbreviation": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сокращение группы'
            }),
            "students_count": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество учащихся'
            }),
            "color": TextInput(attrs={
                'class': 'form-control',
                'type': 'color',
                'placeholder': 'Цвет'
            })
        }


class SubjectsForm(forms.ModelForm):
    cabinets = forms.ModelChoiceField(
        queryset=Cabinets.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Аудитории'})
    )

    class Meta:
        model = Subjects
        fields = ['title', 'abbreviation', 'cabinets', 'color']

        widgets = {
            "title": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название предмета'
            }),
            "abbreviation": forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Сокращение предмета'
            }),
            "color": forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'color',
                'placeholder': 'Цвет'
            })
        }


class TeachersForm(ModelForm):
    class Meta:
        model = Teachers
        fields = ['name', 'abbreviation', 'position', 'subjects', 'cabinets', 'color']

        widgets = {
            "name": TextInput(attrs={'class': 'form-control', 'placeholder': 'Преподаватель'}),
            "abbreviation": TextInput(attrs={'class': 'form-control', 'placeholder': 'Сокращение'}),
            "position": TextInput(attrs={'class': 'form-control', 'placeholder': 'Должность'}),
            "subjects": SelectMultiple(attrs={'class': 'form-control'}),
            "cabinets": SelectMultiple(attrs={'class': 'form-control'}),
            "color": TextInput(attrs={'class': 'form-control', 'type': 'color', 'placeholder': 'Цвет'}),
        }


BUILDING_CHOICES = [
    ('Садовая 218', 'Садовая 218'),
    ('Красноармейская 51', 'Красноармейская 51'),
    ('Новокузнечная 67', 'Новокузнечная 67'),
    ('Леваневского 187/1', 'Леваневского 187/1'),
    ('Тополинная аллея 2/1', 'Тополинная аллея 2/1'),
]


class CabinetsForm(forms.ModelForm):
    building = forms.ChoiceField(choices=BUILDING_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Cabinets
        fields = ['title', 'abbreviation', 'seat_number', 'building', 'color']

        widgets = {
            "title": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
            "abbreviation": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Сокращение'}),
            "seat_number": forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Количество мест'}),
            "color": forms.TextInput(attrs={'class': 'form-control', 'type': 'color', 'placeholder': 'Цвет'}),
        }


class SchedulesForm(ModelForm):
    class Meta:
        model = Schedules
        fields = ['title', 'week_date', 'week_days', 'lessons_counts', 'week_type']
        widgets = {
            "title": TextInput(attrs={'class': 'form-control', 'placeholder': 'Название'}),
            "week_date": DateInput(attrs={'class': 'form-control', 'placeholder': 'Дата', 'type': 'date'}),
            "week_days": forms.SelectMultiple(attrs={'class': 'form-control', 'id': 'example-getting-started'}),
            "lessons_counts": TextInput(attrs={'class': 'form-control', 'placeholder': 'Уроков в день'}),
            "week_type": TextInput(attrs={'class': 'form-control', 'placeholder': 'Тип недели'}),
        }


class BellsForm(ModelForm):
    class Meta:
        model = Bells
        fields = ['time_start', 'time_end', 'type']

        widgets = {
            "time_start": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Начало урока'
            }),
            "time_end": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Конец урока',
                'type': 'date'
            }),
            "type": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тип недели'
            })
        }


class WorkLoadsForm(ModelForm):
    subjects = forms.ModelChoiceField(
        queryset=Subjects.objects.all(),
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'placeholder': 'Предмет'
            })
    )
    class Meta:
        model = WorkLoads

        fields = ['subjects', 'groups', 'teachers', 'cabinets', 'lessons_count']

        widgets = {
            "groups": SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'Группы',
            }),
            "teachers": SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'Преподаватель',
            }),
            "cabinets": SelectMultiple(attrs={
                'class': 'form-control',
                'placeholder': 'Кабинеты',
            }),
            "lessons_count": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Количество уроков'
            })
        }
