# Generated by Django 3.0.6 on 2020-07-05 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0050_auto_20200705_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='color',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='element',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='element',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tree',
            name='color',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Color'),
        ),
    ]