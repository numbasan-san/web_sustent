# Generated by Django 4.1.10 on 2023-08-22 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0089_log_entry_data_json_null_to_object'),
        ('home', '0032_remove_nuevoinforme_tipo'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Indicador',
            new_name='Indicadores',
        ),
    ]
