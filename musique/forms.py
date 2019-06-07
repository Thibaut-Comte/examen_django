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

    def clean_message(self):
        message = self.cleaned_data['message']
        if "blog" in message:
            raise forms.ValidationError("Nous ne sommes pas sur un blog")

