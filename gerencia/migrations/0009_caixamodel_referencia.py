# Generated by Django 2.2.4 on 2020-01-30 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0008_caixamodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='caixamodel',
            name='referencia',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
