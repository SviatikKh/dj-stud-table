from django.forms import ModelForm
from django import forms
from .models import Student


class StudentForm(ModelForm):

    class Meta:
        model = Student
        fields = ['name', 'surname', 'patronymic', 'group']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'patronymic': forms.TextInput(attrs={'class': 'form-control'}),
            'group': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def create(self):
        new_student = Student.objects.create(name=self.cleaned_data['name'],
                                             surname=self.cleaned_data['surname'],
                                             patronymic=self.cleaned_data['patronymic'],
                                             group=self.cleaned_data['group'])
        return new_student

