# Generated by Django 5.1.2 on 2024-12-01 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_remove_usuario_perfil'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]