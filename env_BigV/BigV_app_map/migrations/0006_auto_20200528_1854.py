# Generated by Django 3.0.5 on 2020-05-28 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BigV_app_map', '0005_auto_20200528_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dados_mapeamento',
            name='cnpj',
            field=models.CharField(max_length=14),
        ),
        migrations.AlterField(
            model_name='dados_mapeamento',
            name='site',
            field=models.URLField(),
        ),
    ]