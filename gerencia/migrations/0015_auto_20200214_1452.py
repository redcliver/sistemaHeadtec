# Generated by Django 2.2.4 on 2020-02-14 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0014_produtomodel_subproduto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produtomodel',
            name='prodserv',
        ),
        migrations.AlterField(
            model_name='produtomodel',
            name='unidade',
            field=models.CharField(choices=[('1', 'N/A'), ('2', 'Metro'), ('3', 'Unidade'), ('4', 'Hora'), ('5', 'Dia')], default=1, max_length=1),
        ),
    ]