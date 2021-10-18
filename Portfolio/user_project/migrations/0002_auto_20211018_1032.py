# Generated by Django 3.1.4 on 2021-10-18 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user_project', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproject',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='user_profile.user'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userproject',
            name='project_name',
            field=models.CharField(max_length=255),
        ),
    ]
