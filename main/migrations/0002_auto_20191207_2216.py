# Generated by Django 2.2.5 on 2019-12-08 01:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hospital',
            options={'ordering': ('nombre',), 'verbose_name': 'Hospital', 'verbose_name_plural': 'Hospitales'},
        ),
    ]
