# Generated by Django 2.2.4 on 2020-01-30 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0009_caixamodel_referencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='caixamodel',
            name='desconto',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
