# Generated by Django 3.1.6 on 2021-06-07 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='picture',
            field=models.ImageField(blank=True, default='users/pictures/default-profile.png', upload_to='users/pictures'),
        ),
    ]
