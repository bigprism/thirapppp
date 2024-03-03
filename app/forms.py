from django import forms

from .models import Task



class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('description', 'status')

    def clean_description(self):
        description = self.cleaned_data['description']
        if len(description) < 5:
            raise forms.ValidationError('Description must be at least 5 characters long.')
        return description