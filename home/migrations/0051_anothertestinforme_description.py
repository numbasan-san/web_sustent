# Generated by Django 4.1.10 on 2023-08-29 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0050_alter_anothertestinforme_buroku'),
    ]

    operations = [
        migrations.AddField(
            model_name='anothertestinforme',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]