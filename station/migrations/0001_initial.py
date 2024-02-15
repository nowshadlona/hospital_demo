# Generated by Django 4.2.7 on 2024-02-13 21:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('division', '0001_initial'),
        ('district', '0002_rename_districtname_districts_districtname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('dis_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='district.districts')),
                ('div_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='division.divisions')),
            ],
        ),
    ]