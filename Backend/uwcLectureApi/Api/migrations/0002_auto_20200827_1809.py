# Generated by Django 3.1 on 2020-08-27 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lecturevideos',
            name='video',
            field=models.FileField(upload_to='lectures'),
        ),
    ]
