from django import forms
from .models import Artiste, Album

class ArtisteForm(forms.ModelForm):
    class Meta:
        model = Artiste
        fields = '__all__'

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = '__all__'

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    envoyeur = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

