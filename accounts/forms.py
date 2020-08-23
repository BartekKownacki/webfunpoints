from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms.widgets import TextInput, PasswordInput
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class CreateUserForm(UserCreationForm):
    username = forms.RegexField(
        label=_("Login"), max_length=30, regex=r"^[\w.@+-]+$",
        help_text=_("Required. 30 characters or fewer. Letters, digits and "
                    "@/./+/-/_ only."),
        error_messages={
            'invalid': _("This value may contain only letters, numbers and "
                         "@/./+/-/_ characters.")},
        widget=TextInput(attrs={'class': 'form-control',
                                'required': 'true',
                                'placeholder': 'Login',
                                'style': 'width:200px;margin-bottom:5px;',
                                })
    )
    email = forms.CharField(
        label=_("Email"),
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'email',
                                      'placeholder': 'Adres Email',
                                      'required': 'true',
                                      'style':'width:200px;margin-bottom:5px;',
                                      })
    )
    password1 = forms.CharField(
        label=_("Password"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'type': 'password',
                                          'required': 'true',
                                          'placeholder': 'Hasło',
                                          'style': 'width:200px;margin-bottom:5px;',

        })
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'class': 'form-control',
                                          'type': 'password',
                                          'required': 'true',
                                          'placeholder': 'Powtórz hasło',
                                          'style': 'width:200px;margin-bottom:5px;',
        }),
    )





