# Generated by Django 4.0.4 on 2022-06-06 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0019_doencas_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doencas',
            name='id',
        ),
    ]
