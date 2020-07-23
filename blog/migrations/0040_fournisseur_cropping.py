# Generated by Django 3.0.6 on 2020-07-22 19:24

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0039_auto_20200720_2101'),
    ]

    operations = [
        migrations.AddField(
            model_name='fournisseur',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '200x200', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
