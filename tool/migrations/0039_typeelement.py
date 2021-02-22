# Generated by Django 3.0.6 on 2020-07-03 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tool', '0038_delete_typeelement'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeElement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('description', models.TextField(max_length=30, verbose_name='Description')),
                ('order', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Type of Element',
            },
        ),
    ]
