# Generated by Django 2.2 on 2019-08-31 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190901_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='rating',
            name='comment',
            field=models.TextField(default='This was an awesome place!!'),
        ),
        migrations.AddField(
            model_name='rating',
            name='rate',
            field=models.IntegerField(default=5),
        ),
    ]