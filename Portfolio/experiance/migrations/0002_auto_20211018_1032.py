# Generated by Django 3.1.4 on 2021-10-18 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('experiance', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userexperiance',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='userexperiance',
            name='started_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]