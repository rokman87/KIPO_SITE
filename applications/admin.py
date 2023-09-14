from django.contrib import admin
from .models import Schedules, WorkLoads, Groups, Subjects, Teachers, Cabinets, Bells, WeekDay

admin.site.register(Schedules)
admin.site.register(WorkLoads)
admin.site.register(Groups)
admin.site.register(Subjects)
admin.site.register(Teachers)
admin.site.register(Cabinets)
admin.site.register(Bells)
admin.site.register(WeekDay)