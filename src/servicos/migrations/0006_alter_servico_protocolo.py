# Generated by Django 4.2 on 2023-05-04 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0005_alter_servico_protocolo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='protocolo',
            field=models.CharField(blank=True, max_length=52, null=True),
        ),
    ]
