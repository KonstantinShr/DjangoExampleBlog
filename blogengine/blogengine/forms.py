from django import forms
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    email = forms.CharField()
    password = forms.CharField()

    email.widget.attrs.update({'class': 'form-control'})
    password.widget.attrs.update({'class': 'form-control'})


class RegistrationForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput(), max_length=20)
    first_name = forms.CharField(max_length = 20)
    last_name = forms.CharField(max_length = 20)
    nickname = forms.CharField(max_length = 20)

    email.widget.attrs.update({'class': 'form-control', 'placeholder': 'example@mail.com'})
    password.widget.attrs.update({'class': 'form-control', 'placeholder': '********'})
    first_name.widget.attrs.update({'class': 'form-control', 'placeholder': 'John'})
    last_name.widget.attrs.update({'class': 'form-control', 'placeholder': 'Lenon'})
    nickname.widget.attrs.update({'class': 'form-control', 'placeholder': 'Dr. House'})

    def clean_all(self):
        new_user = {
            'email': self.cleaned_data['email'],
            'password': self.cleaned_data['password'],
            'first_name': self.cleaned_data['first_name'],
            'last_name': self.cleaned_data['last_name'],
            'nickname': self.cleaned_data['nickname'],
        }
        return new_user
