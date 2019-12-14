from django import forms
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    userBirth = forms.DateField()

    class Meta:
        model = User
        fields = ('username', 'password', 'userBirth')
        widgets = {
            'username': forms.TextInput(),
            'password': forms.PasswordInput(),
            'userBirth': forms.DateField(),
        }