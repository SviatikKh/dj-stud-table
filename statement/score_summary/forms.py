from django import forms


class ScoresummaryForm(forms.Form):
    point = forms .CharField(max_length=5, min_length=1, required=True,
                             error_messages={'required': 'Введіть правельну оцінку'})

    def clean_point(self):
        p = self.cleaned_data['point']

        if int(p) > 12 or int(p) < 1:
            raise ValueError('Оцінка від 1 до 12')
        return p
