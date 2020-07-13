# Generated by Django 3.0.6 on 2020-07-13 07:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0037_auto_20200713_0908'),
        ('tool', '0057_tree_linked'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tree',
            options={'ordering': ['-order'], 'verbose_name': 'Arbre'},
        ),
        migrations.AddField(
            model_name='tree',
            name='max_category_column',
            field=models.IntegerField(default=5, verbose_name='Max count of Category'),
        ),
        migrations.AlterField(
            model_name='element',
            name='categorie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Categorie', verbose_name='Catégorie'),
        ),
        migrations.AlterField(
            model_name='element',
            name='color',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Couleur'),
        ),
        migrations.AlterField(
            model_name='element',
            name='fournisseur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Fournisseur', verbose_name='Fournisseur'),
        ),
        migrations.AlterField(
            model_name='element',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='../static', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='element',
            name='minRowWidth',
            field=models.IntegerField(default=1, verbose_name='Largeur minimale'),
        ),
        migrations.AlterField(
            model_name='element',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Ordre'),
        ),
        migrations.AlterField(
            model_name='element',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Service', verbose_name='Service'),
        ),
        migrations.AlterField(
            model_name='element',
            name='sous_categorie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Sous_Categorie', verbose_name='Sous Catégorie'),
        ),
        migrations.AlterField(
            model_name='element',
            name='subTitle',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='SousTitre'),
        ),
        migrations.AlterField(
            model_name='element',
            name='title',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Titre'),
        ),
        migrations.AlterField(
            model_name='element',
            name='typeElemnt',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tool.TypeElement', verbose_name='Type Elément'),
        ),
        migrations.AlterField(
            model_name='node',
            name='color',
            field=models.CharField(max_length=10, null=True, verbose_name='Couleur'),
        ),
        migrations.AlterField(
            model_name='node',
            name='element_father',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tree_fathers', to='tool.Element', verbose_name='Element Père'),
        ),
        migrations.AlterField(
            model_name='node',
            name='father',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tool.Node', verbose_name='Père'),
        ),
        migrations.AlterField(
            model_name='node',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Ordre'),
        ),
        migrations.AlterField(
            model_name='node',
            name='rowWidth',
            field=models.IntegerField(default=1, verbose_name='Largeur'),
        ),
        migrations.AlterField(
            model_name='node',
            name='subTitle',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Sous Titre'),
        ),
        migrations.AlterField(
            model_name='node',
            name='title',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Titre'),
        ),
        migrations.AlterField(
            model_name='node',
            name='tree',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tool.Tree', verbose_name='Arbre'),
        ),
        migrations.AlterField(
            model_name='tree',
            name='color',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Couleur'),
        ),
        migrations.AlterField(
            model_name='tree',
            name='in_home',
            field=models.BooleanField(default=False, verbose_name='Présent'),
        ),
        migrations.AlterField(
            model_name='tree',
            name='linked',
            field=models.BooleanField(default=True, verbose_name='Ancré'),
        ),
        migrations.AlterField(
            model_name='tree',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Titre'),
        ),
        migrations.AlterField(
            model_name='tree',
            name='order',
            field=models.IntegerField(default=0, verbose_name='Ordre'),
        ),
        migrations.AlterField(
            model_name='tree',
            name='rowWidth',
            field=models.IntegerField(default=1, verbose_name='Largeur'),
        ),
    ]
