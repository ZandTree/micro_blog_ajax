# Generated by Django 2.0.1 on 2018-12-01 23:03

import backend.profiles.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nike', models.CharField(blank=True, max_length=100, null=True, verbose_name='НикНейм')),
                ('avatar', models.ImageField(blank=True, null=True, upload_to=backend.profiles.models.get_path_upload_avatar, verbose_name='Аватар')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name_plural': 'Профили',
                'verbose_name': 'Профиль',
            },
        ),
    ]