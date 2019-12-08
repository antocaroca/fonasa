# Generated by Django 2.2.5 on 2019-12-08 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20191208_0133'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='edad',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='n_hist_clinica',
            field=models.PositiveIntegerField(verbose_name='N° historia clínica'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='nombre',
            field=models.CharField(max_length=60),
        ),
    ]
