# Generated by Django 2.2 on 2018-08-23 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180822_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='membership',
            name='prize',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]