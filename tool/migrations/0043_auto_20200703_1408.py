# Generated by Django 3.0.6 on 2020-07-03 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0042_auto_20200703_1308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='element',
            name='color',
            field=models.CharField(max_length=10, null=True, verbose_name='Color'),
        ),
        migrations.AlterField(
            model_name='element',
            name='typeElemnt',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tool.TypeElement', verbose_name='Type of Element'),
        ),
        migrations.AlterField(
            model_name='element',
            name='url',
            field=models.URLField(blank=True, null=True, verbose_name='Description'),
        ),
        migrations.CreateModel(
            name='Tree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_root', models.BooleanField(default=False)),
                ('description', models.TextField(blank=True, max_length=30, null=True, verbose_name='Description')),
                ('color', models.CharField(max_length=10, null=True, verbose_name='Color')),
                ('rowWidth', models.IntegerField(default=1, verbose_name='Width')),
                ('order', models.IntegerField()),
                ('element', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tree_children', to='tool.Element', verbose_name='Element')),
                ('element_father', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tree_fathers', to='tool.Element', verbose_name='Element')),
                ('root', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tool.Tree', verbose_name='Tree')),
            ],
            options={
                'verbose_name': 'Tree',
                'ordering': ['-root', '-element_father', '-order'],
            },
        ),
    ]
