# Generated by Django 4.0.4 on 2022-06-04 01:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0007_alter_usuarios_posto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='localidades',
            name='nome',
        ),
    ]
