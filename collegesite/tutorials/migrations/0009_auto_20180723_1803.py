# Generated by Django 2.2 on 2018-07-23 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0008_auto_20180723_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='slug',
            field=models.SlugField(allow_unicode=True, editable=False, unique=True),
        ),
    ]
