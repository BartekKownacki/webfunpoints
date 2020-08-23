"""funpoints URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from addpoints.views import pointsview, addvalue, PointsApiView
from accounts.views import registerView, loginView, logoutView, welcomeView, historyView
from qanda.views import faqView, faqeditView
from contact.views import contactform
urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('?adminpanel1029/', admin.site.urls, name='admin_panel'),
    path('', welcomeView, name='home'),
    path('points', pointsview, name='points'),
    path('login/', loginView, name='login'),
    path('register/', registerView, name='register'),
    path('logout/', logoutView, name='logout'),
    path('addvalue/', addvalue, name='addvalue'),
    path('history/', historyView, name='history'),
    path('faq/', faqView, name='faq'),
    path('faq/id=<int:pk>/', faqeditView, name='faqedit'),
    path('contact/', contactform, name='contact'),
    path('api/',PointsApiView.as_view(), name='api'),
]
