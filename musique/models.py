from django.db import models

class Album(models.Model):

    name = models.CharField(max_length=255)
    infos = models.TextField(null=True)
    musiques = models.TextField(null=True)
    artistes = models.ManyToManyField('Artiste', related_name='artistes')

    class Meta:
        verbose_name = 'Album'
        ordering = ['name']

    def __str__(self):

        return self.name

class Artiste(models.Model):

    name = models.CharField(max_length=255)
    bio = models.TextField()
    albums = models.ManyToManyField('Album', related_name='albums', blank=True)

    class Meta:
        verbose_name = 'Artiste'
        ordering = ['name']

    def __str__(self):

        return self.name




