# Generated by Django 3.1.7 on 2021-07-12 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mobApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specs',
            name='dimensions',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='specs',
            name='weight',
            field=models.CharField(max_length=10),
        ),
    ]
