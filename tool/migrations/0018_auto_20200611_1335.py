# Generated by Django 3.0.6 on 2020-06-11 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0017_auto_20200611_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(null='False', upload_to='img/'),
        ),
    ]
