# Generated by Django 3.0.6 on 2020-06-23 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0033_auto_20200623_1745'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fournisseur',
            name='services',
        ),
        migrations.AddField(
            model_name='fournisseur',
            name='services',
            field=models.ManyToManyField(to='tool.Service'),
        ),
    ]
