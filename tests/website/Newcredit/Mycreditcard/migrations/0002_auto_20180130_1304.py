# Generated by Django 2.0.1 on 2018-01-30 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mycreditcard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountdatas',
            name='birthday',
            field=models.DateField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='accountdatas',
            name='identifyId',
            field=models.IntegerField(max_length=18, null=True),
        ),
    ]
