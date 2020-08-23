from django.db import models

# Create your models here.
class QandaModel(models.Model):
    question = models.TextField(max_length=150)
    answer = models.TextField(default="Poczekaj! Niedługo odpowiem na Twoje pytanie!", blank=True)
    publish = models.BooleanField(default=False,blank=True)