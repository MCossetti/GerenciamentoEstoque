# Generated by Django 5.1.2 on 2024-11-27 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0003_categoria_produto_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produto',
            name='categoria',
        ),
        migrations.AlterField(
            model_name='produto',
            name='nome',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nome:'),
        ),
    ]
