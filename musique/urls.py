from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('ajouter-artiste', views.newArtiste, name="new-artiste"),
    path('ajouter-album', views.newAlbum, name='new-album'),
    path('artiste/<int:id>', views.viewArtiste, name="view-artiste"),
    path('album/<int:id>', views.viewAlbum, name="view-album"),
    path('artiste/update/<int:id>', views.updateArtiste, name="update-artiste"),
    path('artiste/delete/<int:id>', views.deleteArtiste, name="delete-artiste"),
    path('album/update/<int:id>', views.updateAlbum, name="update-album"),
    path('album/delete/<int:id>', views.deleteAlbum, name="delete-album"),
    path('contact', views.contact, name="contact")
]
