# Generated by Django 2.2.5 on 2019-12-08 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20191207_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='cantidad_pacientes',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='estado',
            field=models.CharField(choices=[('OCU', 'Ocupada'), ('ESP', 'Espera de atención')], max_length=50),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='id_consulta',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='tipo_consulta',
            field=models.CharField(choices=[('PED', 'Pediatría'), ('URG', 'Urgencia'), ('CGI', 'Consulta General Integral')], max_length=50),
        ),
    ]