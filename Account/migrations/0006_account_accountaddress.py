# Generated by Django 2.1.7 on 2019-03-14 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_auto_20190314_0926'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='accountAddress',
            field=models.CharField(default='', max_length=3),
        ),
    ]
