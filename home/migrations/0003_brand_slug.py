# Generated by Django 4.2.2 on 2023-07-10 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_custumerreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.CharField(default='', max_length=500),
        ),
    ]