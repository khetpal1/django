from django import forms
from django.contrib.auth import get_user_model

User=get_user_model()
class Contactform(forms.Form):

    fullname= forms.CharField(widget=forms.TextInput(attrs={'class':"form-control",  "placeholder":"fullname"}))
    email= forms.EmailField(widget=forms.EmailInput(attrs={'class':"form-control",  "placeholder":"Email"}))
    Comment= forms.CharField(widget=forms.Textarea(attrs={'class':"form-control",  "placeholder":"Message"}))


    def clear_email(self):
        email=self.cleaned_data.get("email")
        if not "gmail.com" in email:
            raise forms.ValidationError("email has to be gail.com")
        return email

