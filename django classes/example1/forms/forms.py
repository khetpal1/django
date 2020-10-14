from django import forms
from django.core.exceptions import ValidationError
from django.core import validators
# BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
# FAVORITE_COLORS_CHOICES = [
#     ('blue', 'Blue'),
#     ('green', 'Green'),
#     ('black', 'Black'),
# ]

def name_start(value):
    if value[1]!="a":
        raise forms.ValidationError("your second charatcer should start with a")
def name_start1(value):
    if len(value)<5:
        raise forms.ValidationError("you are on wrong path")

class userregistration(forms.Form):

    name = forms.CharField(validators=[name_start, name_start1])
    email = forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label="again password", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data=super().clean()
        value= self.cleaned_data['password']
        value1= self.cleaned_data['rpassword']
        if value!=value1:
            raise forms.ValidationError("password dont match")
    
