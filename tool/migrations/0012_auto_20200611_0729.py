# Generated by Django 3.0.6 on 2020-06-11 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0011_auto_20200611_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(null='False', upload_to='.../gallery/'),
        ),
    ]