# Generated by Django 4.0.4 on 2022-06-03 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0006_rename_ususarios_usuarios'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuarios',
            name='posto',
            field=models.CharField(choices=[('CIV', 'Servidor Civil'), ('SD', 'Soldado'), ('CB', 'Cabo'), ('SGT', 'Sargento'), ('ST', 'Subtenete'), ('ASP', 'Aspirante'), ('TEN', 'Tenente'), ('CAP', 'Capitao'), ('MAJ', 'Major'), ('TC', 'Tenente Coronel'), ('CEL', 'Coronel'), ('GEN', 'General')], max_length=100),
        ),
    ]