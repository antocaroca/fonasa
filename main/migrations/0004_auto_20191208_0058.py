# Generated by Django 2.2.5 on 2019-12-08 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20191207_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='nombre',
            field=models.CharField(max_length=60),
        ),
    ]