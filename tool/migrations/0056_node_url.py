# Generated by Django 3.0.6 on 2020-07-08 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0055_auto_20200708_0004'),
    ]

    operations = [
        migrations.AddField(
            model_name='node',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
