from django import forms

class TodoCreateForm(forms.Form):
    title = forms.CharField(required=False)
    body = forms.CharField()
    created = forms.DateTimeField()

