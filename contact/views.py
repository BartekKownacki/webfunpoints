from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import contactForm
# Create your views here.
def contactform(request):
    form = contactForm()
    if request.method=="POST":
        form = contactForm(request.POST)
        if form.is_valid():
            send_mail(
                form.cleaned_data['title'],
                'Treść wiadomości: '+ form.cleaned_data['content'] + '\n Adres Email: ' + form.cleaned_data['email'],
                form.cleaned_data['email'],
                ['barti713@gmail.com'],
                fail_silently=False,
            )
    context = {
        'form':form,
    }
    return render(request, 'contact.html', context)