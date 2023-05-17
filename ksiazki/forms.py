from django import forms
from django.core.exceptions import ValidationError

from ksiazki.models import *


class AddAuthorForm(forms.Form):
    first_name = forms.CharField(max_length=16)
    last_name = forms.CharField(max_length=64)
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))


class AddBookForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        author = cleaned_data['author']
        year = cleaned_data['year']
        if author.birth_date.year > year:
            raise ValidationError('Author could not write that book in this year')
        return cleaned_data

    class Meta:
        model = Book
        fields = ['author', 'publisher', 'year', 'title', 'categories']  # lub wymieniać po kolei
        widgets = {
            'categories': forms.CheckboxSelectMultiple
        }


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
