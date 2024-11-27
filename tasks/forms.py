from django.forms import ModelForm
from django.forms.widgets import DateTimeInput
from .models import Task

class TaskForm(ModelForm):
    class Meta:
        model=Task
        fields=["title","due_date"]
        widgets={
            'due_date':DateTimeInput(attrs={'type':'date'}),

        }

