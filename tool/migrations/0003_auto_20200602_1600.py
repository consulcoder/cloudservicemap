# Generated by Django 3.0.6 on 2020-06-02 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0002_auto_20200602_1555'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Servicio',
            new_name='Service',
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Service'},
        ),
    ]