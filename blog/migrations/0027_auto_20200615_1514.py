# Generated by Django 3.0.6 on 2020-06-15 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_service_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fournisseur',
            name='image',
            field=models.ImageField(null='False', upload_to='static/'),
        ),
    ]
