# Generated by Django 2.2.4 on 2020-01-29 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0003_orcamentomodel_produtoitemmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orcamentomodel',
            name='estado',
            field=models.CharField(choices=[('1', 'Aberto'), ('2', 'Finalizado'), ('3', 'Cancelado')], default=1, max_length=1),
        ),
        migrations.AlterField(
            model_name='orcamentomodel',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]