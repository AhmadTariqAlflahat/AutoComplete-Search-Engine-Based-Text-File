# Generated by Django 2.1.2 on 2018-10-23 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='documents/%Y/%m/%d'),
        ),
    ]
