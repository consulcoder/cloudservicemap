# Generated by Django 3.0.6 on 2020-07-05 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0049_auto_20200705_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='title',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Title'),
        ),
    ]
