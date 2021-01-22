# Generated by Django 3.1.5 on 2021-01-22 11:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20210120_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerinformation',
            name='DOR',
        ),
        migrations.AddField(
            model_name='customerinformation',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
