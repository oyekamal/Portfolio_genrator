# Generated by Django 3.1.4 on 2021-10-15 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='image/default.jpg', upload_to='image/'),
        ),
    ]
