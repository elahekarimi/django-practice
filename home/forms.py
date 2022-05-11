from django import forms
from .models import Todo

class TodoCreateForm(forms.Form):
    title = forms.CharField(required=False)
    body = forms.CharField()
    created = forms.DateTimeField()

class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'body', 'created')



