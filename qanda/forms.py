from django import forms
from .models import QandaModel
class questionForm(forms.ModelForm):
    class Meta:
        model = QandaModel

        fields = {
            'question',
            'answer',
            'publish',
        }

        widgets = {
            'question': forms.TextInput(attrs={
                'class': 'form-control',
                'style':'width:300px; margin-left:5px;margin-bottom:5px;margin-right:5px; float:left',
            'placeholder': 'Twoje pytanie....'}),
            'answer':forms.TextInput(attrs={
                'class': 'form-control',
                'style':'width:300px; margin-left:5px;'})
        }
