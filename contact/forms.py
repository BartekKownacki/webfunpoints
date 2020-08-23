from django import forms

class contactForm(forms.Form):
    title = forms.CharField(label="Tytuł",widget=forms.TextInput(attrs={'class': 'form-control',
                                                                        'required': 'true',
                                                                        'placeholder': 'Tytuł',
                                                                        'style': 'width:200px;margin-bottom:5px;',}))
    content = forms.CharField(label="Treść",widget=forms.Textarea(attrs={'class': 'form-control',
                                                                        'required': 'true',
                                                                        'placeholder': 'Treść',
                                                                        'style': 'resize:none;margin-bottom:5px;;width:500px',
                                                                        'rows':8,}))
    email = forms.EmailField(label="Twój adres e-mail",widget=forms.EmailInput(attrs={'class': 'form-control',
                                                                        'required': 'true',
                                                                        'placeholder': 'Twój adres e-mail',
                                                                        'style': 'width:200px;margin-bottom:5px;',}))

