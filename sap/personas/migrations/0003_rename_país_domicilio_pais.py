# Generated by Django 4.2 on 2023-04-28 18:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0002_domicilio_persona_domicilio'),
    ]

    operations = [
        migrations.RenameField(
            model_name='domicilio',
            old_name='país',
            new_name='pais',
        ),
    ]
