# Generated by Django 4.2 on 2023-04-28 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicos', '0002_alter_servico_protocolo'),
    ]

    operations = [
        migrations.AddField(
            model_name='servico',
            name='indentificador',
            field=models.CharField(blank=True, max_length=24, null=True),
        ),
    ]
