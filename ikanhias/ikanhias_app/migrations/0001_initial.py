# Generated by Django 4.1.2 on 2022-11-01 08:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='jenis',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=9)),
                ('keterangan', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ikan_hias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_ikan', models.CharField(max_length=50)),
                ('asal_ikan', models.CharField(max_length=40)),
                ('harga', models.IntegerField(null=True)),
                ('gambar', models.CharField(max_length=70, null=True)),
                ('penjelasan', models.TextField(null=True)),
                ('jenis_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ikanhias_app.jenis')),
            ],
        ),
    ]
