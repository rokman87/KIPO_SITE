from django.urls import path
from . import views
from django.contrib.auth import views as authViews

urlpatterns = [
    path('registration/', views.registration, name="registration"),
    path('login/', views.pagelogin, name="pagelogin"),
    path('home/', views.home, name="home"),
    path('exit/', authViews.LogoutView.as_view(next_page='index'), name='exit'),
]
