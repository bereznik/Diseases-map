# Generated by Django 4.0.4 on 2022-06-06 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0018_alter_notificacoes_idmunicipio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='doencas',
            name='id',
            field=models.IntegerField(auto_created=True, default=0, unique=True),
        ),
    ]
