# Generated by Django 2.2.4 on 2020-01-29 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gerencia', '0004_auto_20200129_0157'),
    ]

    operations = [
        migrations.AddField(
            model_name='produtoitemmodel',
            name='total',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]