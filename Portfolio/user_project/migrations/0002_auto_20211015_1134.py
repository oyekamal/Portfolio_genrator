# Generated by Django 3.1.4 on 2021-10-15 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userproject',
            name='project_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]