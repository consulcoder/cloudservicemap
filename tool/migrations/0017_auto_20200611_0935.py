# Generated by Django 3.0.6 on 2020-06-11 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0016_auto_20200611_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(null='False', upload_to=''),
        ),
    ]
