# Generated by Django 3.0.6 on 2020-06-11 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20200611_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(null='False', upload_to='static/'),
        ),
    ]
