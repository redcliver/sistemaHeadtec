# Generated by Django 2.2.4 on 2020-01-25 04:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='clienteModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(choices=[('1', 'Ativo'), ('2', 'Inativo'), ('3', 'Excluido')], default=1, max_length=1)),
                ('nome', models.CharField(max_length=200)),
                ('telefone', models.CharField(blank=True, max_length=15, null=True)),
                ('cnpj', models.CharField(blank=True, max_length=30, null=True)),
                ('cpf', models.CharField(blank=True, max_length=30, null=True)),
                ('dataNascimento', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('celular', models.CharField(blank=True, max_length=15, null=True)),
                ('email', models.CharField(blank=True, max_length=300, null=True)),
                ('dataCadastro', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
