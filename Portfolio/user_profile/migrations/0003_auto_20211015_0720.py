# Generated by Django 3.1.4 on 2021-10-15 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_user_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='content',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]