# Generated by Django 4.0.4 on 2022-06-05 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0010_delete_notificacoestotal_remove_notificacoes_data_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='localidades',
            old_name='cidade',
            new_name='nome',
        ),
        migrations.AddField(
            model_name='localidades',
            name='regiao',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]