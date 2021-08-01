from django import forms
from .models import Task , CategoryTask


class TaskForm(forms.ModelForm):
    class Meta:
        model=Task
        fields=['title', 'description','pority','category','expire_date']


class CategoryTaskForm(forms.ModelForm):
    class Meta:
        model = CategoryTask
        fields =['category',]





