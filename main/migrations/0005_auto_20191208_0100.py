# Generated by Django 2.2.5 on 2019-12-08 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20191208_0058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='estado',
            field=models.CharField(choices=[('Ocupada', 'Ocupada'), ('Espera', 'Espera de atención')], max_length=50),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='tipo_consulta',
            field=models.CharField(choices=[('Pediatría', 'Pediatría'), ('Urgencia', 'Urgencia'), ('Consulta General Integral', 'Consulta General Integral')], max_length=50),
        ),
    ]
