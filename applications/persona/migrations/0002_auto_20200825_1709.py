# Generated by Django 3.1 on 2020-08-25 23:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='empleado',
            options={'ordering': ['last_name'], 'verbose_name': 'Mi Empleado', 'verbose_name_plural': 'All employees'},
        ),
    ]