# Generated by Django 3.2 on 2021-06-20 08:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0009_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='organization',
            name='edited_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]