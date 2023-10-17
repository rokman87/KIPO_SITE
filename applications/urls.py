from django.urls import path
from . import views
from .views import SaveCellData

urlpatterns = [
    path('<int:app_id>/schedules/', views.schedules, name='schedules'),
    path('<int:app_id>/bells/', views.bells, name='bells'),
    path('<int:app_id>/lessons/', views.lessons, name='lessons'),
    path('<int:app_id>/work_times/', views.work_times, name='work_times'),
    path('<int:app_id>/workloads/', views.workloads, name='workloads'),
    path('<int:app_id>/print/schedule/', views.printSchedule, name='print/schedule'),
    path('<int:app_id>/groups/', views.groups, name='groups'),
    path('<int:app_id>/subjects/', views.subjects, name='subjects'),
    path('<int:app_id>/teachers/', views.teachers, name='teachers'),
    path('<int:app_id>/cabinets/', views.cabinets, name='cabinets'),
    path('<int:app_id>/types_lessons/', views.types_lessons, name='types_lessons'),
    path('<int:app_id>/publication/', views.publication, name='publication'),
    path('<int:app_id>/settings/', views.settings, name='settings'),
    path('ajax/get_workload/<int:workload_id>/', views.get_workload, name='get_workload'),
    path('url-django/', SaveCellData.as_view(), name='save-cell-data'),

]
