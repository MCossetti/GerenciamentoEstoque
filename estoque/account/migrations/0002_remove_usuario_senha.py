# Generated by Django 5.1.2 on 2024-12-01 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='senha',
        ),
    ]
