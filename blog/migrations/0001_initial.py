# Generated by Django 4.0.3 on 2022-04-28 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contacts',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=255)),
                ('content', models.CharField(default='', max_length=500)),
                ('heading', models.CharField(default='', max_length=50)),
                ('author', models.CharField(default='', max_length=130)),
                ('thumbnail', models.ImageField(default='', upload_to='blog')),
                ('punlish_date', models.DateField()),
            ],
        ),
    ]
