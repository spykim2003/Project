# Generated by Django 2.1.7 on 2019-03-14 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='accountEmail',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='account',
            name='accountName',
            field=models.TextField(),
        ),
    ]
