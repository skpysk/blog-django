# Generated by Django 4.0.3 on 2022-04-28 10:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contacts',
            new_name='post',
        ),
    ]
