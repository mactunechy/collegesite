# Generated by Django 2.2 on 2018-08-24 06:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tutorials', '0020_auto_20180824_0014'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registered_student',
            name='student',
        ),
        migrations.AddField(
            model_name='registered_student',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='enrolled_tutorial', to=settings.AUTH_USER_MODEL),
        ),
    ]
