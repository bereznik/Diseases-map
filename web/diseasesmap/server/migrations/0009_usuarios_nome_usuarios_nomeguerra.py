# Generated by Django 4.0.4 on 2022-06-04 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0008_remove_localidades_nome'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='nome',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='nomeguerra',
            field=models.CharField(default='', max_length=20),
        ),
    ]