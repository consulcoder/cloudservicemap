# Generated by Django 3.0.6 on 2020-07-24 12:28

import cropperjs.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0040_fournisseur_cropping'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fournisseur',
            name='cropping',
        ),
        migrations.AlterField(
            model_name='fournisseur',
            name='image',
            field=cropperjs.models.CropperImageField(aspectratio='1.0', dimensions=(200, 200), null='False', upload_to='../static/'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=cropperjs.models.CropperImageField(aspectratio='1.0', dimensions=(200, 200), null='False', upload_to='../static/'),
        ),
    ]
