# Generated by Django 2.2 on 2018-08-23 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0014_auto_20180823_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='length',
            field=models.CharField(default='35:04', max_length=10),
            preserve_default=False,
        ),
    ]
