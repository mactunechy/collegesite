# Generated by Django 2.2 on 2018-08-23 16:53

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0016_course_prize'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='registered_students',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]