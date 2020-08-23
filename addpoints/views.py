from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from .models import pointsmodel
from django.contrib.auth.decorators import login_required
from django.contrib import messages


from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
# Create your views here.

#@login_required(login_url='login')
def pointsview(request):
    if request.user.is_authenticated:
        value = pointsmodel.objects.all().order_by("-id")[0].points
        added = pointsmodel.objects.all().filter(addvalue=1).count()
        divwidth = 200
        divwidth_to_calculations = divwidth - 12
        objamount = pointsmodel.objects.all().count() - 1
        if added != 0:
            greenpointspercent = round(added/objamount * 100)
            redpointspercent = round((objamount-added)/objamount * 100)
            greenpoints = round(divwidth_to_calculations * greenpointspercent / 100)
            redpoints = round(divwidth_to_calculations * redpointspercent / 100)
        else:
            greenpointspercent = 50
            redpointspercent = 50
            greenpoints = round(0.5 * divwidth_to_calculations)
            redpoints = greenpoints
        context={
            'points':value,
            'objamount':objamount,
            'greenpointspercent':greenpointspercent,
            'redpointspercent': redpointspercent,
            'greenpoints': greenpoints,
            'redpoints':redpoints,


        }
        return render(request, 'pointsview.html', context)
    else:
        messages.info(request, 'Najpierw musisz się zalogować!')
        return redirect('login')

@login_required(login_url='login')
def addvalue(request):
    prevalue = pointsmodel.objects.all().order_by("-id")[0].points
    if request.POST.get('comment') == "":
        komentarz = "Bez_komentarza.jpg"
    else:
        komentarz = request.POST.get('comment')

    if request.POST.get('addvalue'):
        mypoints = pointsmodel(points = prevalue + 1,
                               addvalue = 1,
                               dateadded = timezone.now(),
                               addedby=request.user,
                               comment=komentarz)
    elif request.POST.get('decvalue'):
        mypoints = pointsmodel(points=prevalue - 1,
                               addvalue=-1,
                               dateadded=timezone.now(),
                               addedby=request.user,
                               comment=komentarz)

    mypoints.save()
    return redirect('points')


# def PointsApiView(request):
#     pointsvalue = pointsmodel.objects.all().order_by("-id")[0].points
#     data={
#         'value':pointsvalue
#     }
#     return JsonResponse(data)

class PointsApiView(APIView):
    def get(self, request, *args, **kwargs):
        pointsvalue = pointsmodel.objects.all().order_by("-id")[0].points
        data={
            'value':pointsvalue
        }
        return Response(data)