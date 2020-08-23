from django.db import models
from django.utils import timezone
from django.conf import settings
class pointsmodel(models.Model):
    points = models.IntegerField(default=0, blank=True, null=True)
    addvalue = models.IntegerField(default=0)
    dateadded = models.DateTimeField(default=timezone.now())
    addedby = models.TextField(default='Anonymous')
    comment = models.TextField(default='Bez_komentarza.jpg')