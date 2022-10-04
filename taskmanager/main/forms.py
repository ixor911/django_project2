from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'task']
        widgets = {
            'name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Name"
            }),
            'task': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Description"
            })
        }







