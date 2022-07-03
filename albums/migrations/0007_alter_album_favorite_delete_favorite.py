# Generated by Django 4.0.5 on 2022-07-03 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0006_alter_album_favorite_alter_favorite_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='favorite',
            field=models.CharField(choices=[('Favorite', 'Favorite'), ('Not a favorite', 'Not a favorite')], default='Not a favorite', max_length=15),
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]