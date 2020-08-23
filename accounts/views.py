from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from addpoints.models import pointsmodel
from django.core.paginator import Paginator



def registerView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm

        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Konto: ' + user + ' zostało stworzone!')
                return redirect('login')

        context = {
            'form':form,
        }
        return render(request, 'register.html', context)

def loginView(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Login albo hasło zostało źle wprowadzone')
        context = {}
        return render(request, 'login.html', context)

def logoutView(request):
    logout(request)
    return redirect('home')

def welcomeView(request):

    value = pointsmodel.objects.all().order_by("-id")[0].points

    if request.user.is_authenticated:
        name = request.user
    else:
        name = 'Niezarejestrowany'
    context = {
        'name':name,
        'points':value,
    }
    return render(request, 'index.html', context)


def historyView(request):
    obj = pointsmodel.objects.all().order_by("-id")
    paginator = Paginator(obj, 5)
    page = request.GET.get('page')
    obj = paginator.get_page(page)
    context={
        'obj':obj,
    }
    return render(request, 'history.html', context)