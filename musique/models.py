from django.db import models

class Artiste(models.Model):

    name = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255)
    born = models.DateTimeField(verbose_name='Date de naissance')
    bio = models.TextField()
    discographie = models.ForeignKey('Album', on_delete='', null=True)

    class Meta:
        verbose_name = 'Artiste'
        ordering = ['name']

    def __str__(self):

        return self.name

class Album(models.Model):

    name = models.CharField(max_length=255)
    bio = models.TextField()

    class Meta:
        verbose_name = 'Album'
        ordering = ['name']

    def __str__(self):

        return self.name


