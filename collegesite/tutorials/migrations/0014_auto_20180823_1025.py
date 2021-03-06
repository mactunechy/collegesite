# Generated by Django 2.2 on 2018-08-23 08:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tutorials', '0013_course_registered_students'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Registered_students',
            new_name='Registered_student',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tutorials', to='tutorials.Course'),
        ),
    ]
