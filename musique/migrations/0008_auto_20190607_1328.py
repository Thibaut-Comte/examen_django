# Generated by Django 2.2.1 on 2019-06-07 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musique', '0007_auto_20190607_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artiste',
            name='discographie',
            field=models.ManyToManyField(blank=True, related_name='albums', to='musique.Album'),
        ),
    ]
