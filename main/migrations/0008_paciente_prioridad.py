# Generated by Django 2.2.5 on 2019-12-08 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20191208_0135'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='prioridad',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
