from django import forms
from django.forms import ModelForm
from .models import Teacher


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'surname', 'patronymic']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'surname': forms.TextInput(attrs={'class':'form-control'}),
            'patronymic': forms.TextInput(attrs={'class':'form-control'}),
        }

    def create(self):
        new_teacher = Teacher.objects.create(name=self.cleaned_data['name'],
                                             surname=self.cleaned_data['surname'],
                                             patronymic=self.cleaned_data['patronymic'])
        return new_teacher
