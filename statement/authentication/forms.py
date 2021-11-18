from django import forms
from django.forms import ModelForm
from .models import CustomUser


class CustomUserForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email',
                  'password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.TextInput(attrs={'class': 'form-control'})
        }

    def create(self):
        new_user = CustomUser.objects.create(first_name=self.cleaned_data['first_name'],
                                             last_name=self.cleaned_data['last_name'],
                                             email=self.cleaned_data['email'],
                                             password=self.cleaned_data['password'])
        return new_user
