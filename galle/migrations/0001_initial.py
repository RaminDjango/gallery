# Generated by Django 4.2.1 on 2023-05-24 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InfoPictureAdd',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=400)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
