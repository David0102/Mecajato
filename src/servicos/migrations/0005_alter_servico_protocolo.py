# Generated by Django 4.2 on 2023-05-04 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0004_rename_indentificador_servico_identificador'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='protocolo',
            field=models.CharField(max_length=52),
        ),
    ]