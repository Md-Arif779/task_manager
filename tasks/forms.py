from django import forms
from .models import Task, TaskImage

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'priority', 'completed']



class TaskImageForm(forms.ModelForm):
    class Meta:
        model = TaskImage
        fields = ['image']


