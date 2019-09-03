# Generated by Django 2.2.2 on 2019-09-03 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_place_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(max_length=200)),
                ('description', models.TextField(default='Some Description Over here', max_length=1000)),
                ('image', models.ImageField(default='/static/img/logo.png', upload_to='images/')),
            ],
        ),
    ]
