from django import forms
from django.contrib.auth.models import User
# 2 types of forms:
# 1) ModelForm - Based on model field
# 2) Form - Not based on model field


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
                "class": "form-control"})
                              )
    password = forms.CharField(widget=forms.PasswordInput(attrs={
                "class": "form-control"}))


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={
        "class": "form-control"
    })
                               )
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput(attrs={
        "class": "form-control"
    })
                                )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        widgets = {
            "username": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "first_name": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "last_name": forms.TextInput(attrs={
                "class": "form-control"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control"
            })
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords are not similar')
        return cd['password2']
