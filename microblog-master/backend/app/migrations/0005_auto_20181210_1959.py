# Generated by Django 2.0.1 on 2018-12-10 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_post_user_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='twit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments', to='app.Post', verbose_name='Твит'),
        ),
    ]
