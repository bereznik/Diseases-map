# Generated by Django 4.0.4 on 2022-05-30 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0005_localidades_notificacoes_notificacoestotal_ususarios'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Ususarios',
            new_name='Usuarios',
        ),
    ]
