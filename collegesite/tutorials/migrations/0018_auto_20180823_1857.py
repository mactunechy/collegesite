# Generated by Django 2.2 on 2018-08-23 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0017_auto_20180823_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='prize',
            field=models.FloatField(),
        ),
    ]
