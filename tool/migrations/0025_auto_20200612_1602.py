# Generated by Django 3.0.6 on 2020-06-12 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0024_auto_20200612_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='statut',
            field=models.BooleanField(default=True),
        ),
    ]