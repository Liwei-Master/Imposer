from django import forms

class UserForm(forms.Form):
    """docstring for UserForm"""
    username = forms.CharField(max_length=30)
    password = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=30,required=False)
    facebook = forms.CharField(max_length=30,required=False)

