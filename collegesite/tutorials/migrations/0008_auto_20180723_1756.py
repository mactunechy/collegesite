# Generated by Django 2.2 on 2018-07-23 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0007_auto_20180723_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='slug',
            field=models.SlugField(allow_unicode=True, unique=True),
        ),
    ]
