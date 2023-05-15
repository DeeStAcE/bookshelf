from django import forms


class AddAuthorForm(forms.Form):
    first_name = forms.CharField(max_length=16)
    last_name = forms.CharField(max_length=64)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
