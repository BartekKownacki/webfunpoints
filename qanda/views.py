from django.shortcuts import render, redirect, get_object_or_404
from .models import QandaModel
from .forms import questionForm
from django.core.paginator import Paginator

# Create your views here.

def faqView(request):
    myform = questionForm(request.POST)
    if request.POST.get('submit'):
        if myform.is_valid():
            myform.save()
        else:
            print("Dodaj messages")

    objects = QandaModel.objects.all().order_by("-id")
    paginator = Paginator(objects, 5)
    page = request.GET.get('page')
    objects =paginator.get_page(page)
    form = questionForm
    context = {
        'obj': objects,
        'form':form,
    }
    return render(request, 'faq.html', context)

def faqeditView(request, pk):
    questionedit = get_object_or_404(QandaModel, pk=pk)
    if request.method=="POST":
        form = questionForm(request.POST, instance=questionedit)
        if request.POST.get('delete'):
            questionedit.delete()
            return redirect('faq')
        else:
            if form.is_valid():
                questionedit = form.save()
                questionedit.save()
                return redirect('faq')
    else:
        form = questionForm(instance=questionedit)
    context = {
        'obj': form
    }
    return render(request, 'faqedit.html', context)


