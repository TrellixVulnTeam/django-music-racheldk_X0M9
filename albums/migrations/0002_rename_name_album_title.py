# Generated by Django 4.0.5 on 2022-06-30 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='name',
            new_name='title',
        ),
    ]