# Generated by Django 3.0.6 on 2020-06-12 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0023_auto_20200612_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='statut',
            field=models.BooleanField(),
        ),
    ]
