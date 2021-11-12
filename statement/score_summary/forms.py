from django.forms import ModelForm
from .models import Scoresummary
from django import forms


# class ScoresummaryForm(ModelForm):
#     class Meta:
#         model = Scoresummary
#         fields = ['student', 'point', 'subject']

    # def clean_point(self):
    #     p = self.cleaned_data['point']
    #
    #     if int(p) > 12 or int(p) < 1:
    #         raise ValueError('Оцінка від 1 до 12')
    #     return p



class ScoresummaryForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        point = forms.CharField(max_length=5, min_length=1, required=True,
                                 error_messages={'required': 'Введіть правельну оцінку'})
        queryset = Scoresummary.objects.all()
        for k, q in enumerate(queryset):
            self.fields[q.pk] = forms.CharField(label=q.student.name)

    # def save(self):
    #     for f in self.fields:
    #



#     def clean_point(self):
#         p = self.cleaned_data['point']
#
#         if int(p) > 12 or int(p) < 1:
#             raise ValueError('Оцінка від 1 до 12')
#         return p
