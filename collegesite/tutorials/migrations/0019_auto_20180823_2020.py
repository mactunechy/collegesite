# Generated by Django 2.2 on 2018-08-23 18:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0018_auto_20180823_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='registered_students',
        ),
        migrations.RemoveField(
            model_name='registered_student',
            name='tutorial',
        ),
        migrations.AddField(
            model_name='registered_student',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='enrolled_students', to='tutorials.Course'),
        ),
        migrations.AlterField(
            model_name='registered_student',
            name='student',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='enrolled_tutorial', to=settings.AUTH_USER_MODEL),
        ),
    ]