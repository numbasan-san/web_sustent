# Generated by Django 4.1.10 on 2023-08-21 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0031_nuevoinforme_tipo_alter_nuevoinforme_estado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nuevoinforme',
            name='tipo',
        ),
    ]
