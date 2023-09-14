from django.contrib import admin
from .models import Schedules, Groups, Subjects, Teachers, Cabinets, Bells, WeekDay, WorkLoads

admin.site.register(Schedules)
admin.site.register(Groups)
admin.site.register(Subjects)
admin.site.register(Teachers)
admin.site.register(Cabinets)
admin.site.register(Bells)
admin.site.register(WeekDay)
admin.site.register(WorkLoads)