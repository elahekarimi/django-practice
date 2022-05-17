from django import forms

class UserRegisterForms(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()

class UserLoginForms(forms.Form):
    username = forms.CharField()
    password = forms.CharField()




