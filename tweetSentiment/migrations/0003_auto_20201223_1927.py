# Generated by Django 3.1.4 on 2020-12-23 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweetSentiment', '0002_auto_20201223_1353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='creation_date',
            field=models.DateField(),
        ),
    ]
