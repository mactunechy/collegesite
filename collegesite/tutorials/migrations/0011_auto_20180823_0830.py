# Generated by Django 2.2 on 2018-08-23 06:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0003_auto_20180822_2209'),
        ('tutorials', '0010_auto_20180809_1823'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tutorial',
            options={'ordering': ['position']},
        ),
        migrations.RenameField(
            model_name='tutorial',
            old_name='prize',
            new_name='position',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='cover_image',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='description',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='lecturer',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='registered_students',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='resources',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='slug',
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('prize', models.IntegerField()),
                ('cover_image', models.FileField(upload_to='lectures/cover_photos')),
                ('slug', models.SlugField(allow_unicode=True, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('resources', models.FileField(blank=True, default='null', null=True, upload_to='resources/')),
                ('lecturer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courses', to=settings.AUTH_USER_MODEL)),
                ('membership', models.ManyToManyField(to='accounts.Membership')),
            ],
        ),
    ]
