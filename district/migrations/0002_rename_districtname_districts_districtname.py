# Generated by Django 4.2.7 on 2024-02-13 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('district', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='districts',
            old_name='districtname',
            new_name='Districtname',
        ),
    ]
