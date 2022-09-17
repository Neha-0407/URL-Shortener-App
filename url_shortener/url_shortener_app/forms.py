from django import forms

class URLform(forms.Form):
    longurl =  forms.URLField(max_length=250)