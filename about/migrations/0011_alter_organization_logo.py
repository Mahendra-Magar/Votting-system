# Generated by Django 3.2 on 2021-06-20 08:30

import about.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0010_auto_20210620_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='logo',
            field=models.ImageField(blank=True, max_length=1024, null=True, upload_to=about.models.upload_about_organization_picture),
        ),
    ]