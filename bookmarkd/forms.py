from django import forms

from .models import Dictionary

class DictionaryForm(forms.ModelForm):
    title = forms.CharField(max_length=8,required=True,label="タイトル")
    description = forms.CharField(max_length=32,required=False,label="　　説明",widget=forms.TextInput)
    url = forms.URLField(required=False,label="　　URL")
    tag = forms.CharField(max_length=256,label="　　タグ")
    class Meta:
        model = Dictionary
        fields = ('title','description','url','tag')