from django import forms

from .models import Dictionary

class DictionaryForm(forms.ModelForm):

    class Meta:
        model = Dictionary
        fields = ('title', 'url', 'tag')