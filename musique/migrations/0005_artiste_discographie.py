# Generated by Django 2.2.1 on 2019-06-07 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musique', '0004_auto_20190607_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='artiste',
            name='discographie',
            field=models.ManyToManyField(related_name='artistes', to='musique.Album'),
        ),
    ]