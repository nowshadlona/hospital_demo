# Generated by Django 4.2.7 on 2024-02-15 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('station', '0003_remove_station_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='image',
            field=models.ImageField(default=1, upload_to='images/'),
            preserve_default=False,
        ),
    ]
