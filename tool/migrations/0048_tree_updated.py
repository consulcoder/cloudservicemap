# Generated by Django 3.0.6 on 2020-07-04 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0047_tree_root_node'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='updated',
            field=models.BooleanField(default=False),
        ),
    ]
