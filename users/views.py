from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm, ApplicationsForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Applications
from django.contrib.auth.decorators import login_required


def registration(request):
    firstname = ''
    lastname = ''
    emailvalue = ''
    uservalue = ''
    passwordvalue1 = ''
    passwordvalue2 = ''

    form = SignupForm(request.POST or None)
    if form.is_valid():
        fs = form.save(commit=False)
        firstname = form.cleaned_data.get("first_name")
        lastname = form.cleaned_data.get("last_name")
        emailvalue = form.cleaned_data.get("email")
        uservalue = form.cleaned_data.get("username")
        passwordvalue1 = form.cleaned_data.get("password1")
        passwordvalue2 = form.cleaned_data.get("password2")
        if passwordvalue1 == passwordvalue2:
            try:
                user = User.objects.get(username=uservalue)  # if able to get, user exists and must try another username
                context = {'form': form,
                           'error': 'Введенное вами имя пользователя уже занято. Пожалуйста, попробуйте другое имя '
                                    'пользователя.'}
                return render(request, 'users/registration.html', context)
            except User.DoesNotExist:
                user = User.objects.create_user(uservalue, password=passwordvalue1,
                                                email=emailvalue)
                user.save()

                login(request, user)

                fs.user = request.user

                fs.save()
                messages.success(request, 'Регистрация прошла успешно. Пожалуйста, выполните вход.')
                return redirect('/users/login')

        else:
            context = {'form': form, 'error': 'Пароли, которые вы указали, не совпадают'}
            return render(request, 'users/registration.html', context)


    else:
        context = {'form': form}
        return render(request, 'users/registration.html', context)


@login_required
def pagelogin(request):
    uservalue = ''
    passwordvalue = ''

    valuenext = request.POST.get('next')

    form = LoginForm(request.POST or None)
    if form.is_valid():
        uservalue = form.cleaned_data.get("username")
        passwordvalue = form.cleaned_data.get("password")

        user = authenticate(username=uservalue, password=passwordvalue)
        if user is not None and valuenext == '':
            login(request, user)

            context = {'form': form,
                       'valuenext': valuenext}

            messages.success(request, "Вы успешно вошли в систему!")

            return redirect('home')

        if user is not None and valuenext != '':
            login(request, user)

            messages.success(request, "Вы успешно вошли в систему")

            context = {'form': form,
                       'valuenext': valuenext}

            return redirect(valuenext)
        else:
            context = {'form': form,
                       'error': 'Неверная комбинация имени пользователя и пароля'}

            return render(request, 'users/login.html', context)

    else:

        context = {'form': form}
        return render(request, 'users/login.html', context)


def home(request):
    applications = Applications.objects.all()

    error = ''
    if request.method == 'POST':
        form = ApplicationsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма была неверной'

    form = ApplicationsForm()

    data = {
        'form': form,
        'error': error,
        'applications': applications,
    }
    return render(request, 'users/home.html', data)
