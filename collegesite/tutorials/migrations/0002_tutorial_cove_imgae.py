# Generated by Django 2.2 on 2018-07-22 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorial',
            name='cove_imgae',
            field=models.FileField(default=1, upload_to='lectures/cover_photos'),
            preserve_default=False,
        ),
    ]
