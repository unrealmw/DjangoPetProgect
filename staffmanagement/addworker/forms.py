from django.forms import ModelForm
from django import forms

from .models import Worker


class WorkerForm(ModelForm):
    class Meta:
        model = Worker
        fields = ('name', 'last_name', 'patronymic',
                  'birth_date', 'department')
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['birth_date'].input_formats = ['%d-%m-%Y']
