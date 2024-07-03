from django import forms

class CodeForm(forms.Form):
    code = forms.CharField(label='Enter IMDB code for the movie', max_length=10)