from django import forms
from .models import Student
from score_summary.models import Group


class StudentForm(forms.Form):
    choices = tuple(((group.id, group.group) for group in Group.objects.all()))
    name = forms.CharField()
    surname = forms.CharField()
    patronymic = forms.CharField()
    group = forms.ChoiceField(choices=choices)
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
                                             group_id=self.cleaned_data['group'])
        return new_student

