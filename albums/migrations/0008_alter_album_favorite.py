# Generated by Django 4.0.5 on 2022-07-03 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0007_alter_album_favorite_delete_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
    ]