# Generated by Django 3.0.6 on 2020-07-04 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0046_auto_20200704_0605'),
    ]

    operations = [
        migrations.AddField(
            model_name='tree',
            name='root_node',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='root', to='tool.Node', verbose_name='Root'),
        ),
    ]