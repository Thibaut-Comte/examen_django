from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from musique.models import Artiste, Album
from musique.forms import ArtisteForm, AlbumForm, ContactForm

def home(request):

    artistes = Artiste.objects.all()
    albums = Album.objects.all()

    return render(request, 'musique/index.html', {'artistes': artistes, 'albums': albums})

def newArtiste(request):

    form = ArtisteForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data['name']
        bio = form.cleaned_data['bio']
        # discographie = form.cleaned_data['discographie']

        form.save()

        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer

        return redirect('home')

    return render(request, 'musique/Artiste/form.html', locals())

def newAlbum(request):

    form = AlbumForm(request.POST or None)

    if form.is_valid():
        name = form.cleaned_data['name']
        infos = form.cleaned_data['infos']
        musiques = form.cleaned_data['musiques']

        form.save()
        return redirect('home')

    return render(request, 'musique/Album/form.html', locals())

def viewArtiste(request, id):

    artiste = get_object_or_404(Artiste, id=id)

    return render(request, 'musique/Artiste/view.html', {'artiste': artiste})

def viewAlbum(request, id):

    album = get_object_or_404(Album, id=id)

    return render(request, 'musique/Album/view.html', {'album': album})

def updateArtiste(request, id):

    artiste = get_object_or_404(Artiste, id=id)

    form = ArtisteForm(request.POST or None, instance=artiste)

    update = True

    if form.is_valid():
        name = form.cleaned_data['name']
        bio = form.cleaned_data['bio']
        form.save()

        update = True

    return render(request, 'musique/Artiste/form.html', locals())

def updateAlbum(request, id):

    album = get_object_or_404(Album, id=id)

    form = AlbumForm(request.POST or None, instance=album)

    update = True

    if form.is_valid():
        form.save()

        update = True

    return render(request, 'musique/Album/form.html', locals())

def deleteArtiste(request, id):

    artiste = get_object_or_404(Artiste, id=id)

    artiste.delete()

    return redirect('home')

def deleteAlbum(request, id):

    album = get_object_or_404(Album, id=id)

    album.delete()

    return redirect('home')

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        sujet = form.cleaned_data['sujet']
        envoyeur = form.cleaned_data['envoyeur']
        message = form.cleaned_data['message']
        envoi = True

    return render(request, 'musique/contact.html', locals())

