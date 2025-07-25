# Generated by Django 4.2.16 on 2025-06-24 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manaj', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pajak',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_jatuh_tempo', models.DateField()),
                ('nominal', models.DecimalField(decimal_places=2, max_digits=12)),
                ('kendaraan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pajaks', to='manaj.kendaraan')),
            ],
            options={
                'db_table': 'garasi_pajak',
            },
        ),
    ]
