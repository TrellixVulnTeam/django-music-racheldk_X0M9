# Generated by Django 4.0.5 on 2022-07-02 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_artist_rename_title_album_name_alter_album_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
    ]