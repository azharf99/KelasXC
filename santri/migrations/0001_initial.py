# Generated by Django 4.2.4 on 2023-08-02 05:56

from django.db import migrations, models
import django.db.models.deletion
import santri.compress_image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DokumentasiKelas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', santri.compress_image.CompressedImageField(blank=True, default='no-image.png', help_text='format logo .jpg/.jpeg', null=True, quality=50, upload_to='kelas')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='PrestasiKelas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prestasi', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Santri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_santri', models.CharField(max_length=100)),
                ('nis', models.CharField(max_length=100)),
                ('tempat_lahir', models.CharField(blank=True, max_length=100, null=True)),
                ('tanggal_lahir', models.DateField(blank=True, null=True)),
                ('alamat', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PrestasiSantri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prestasi', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('santri', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='santri.santri')),
            ],
        ),
        migrations.CreateModel(
            name='PelanggaranSantri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pelanggaran', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('santri', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='santri.santri')),
            ],
        ),
        migrations.CreateModel(
            name='HafalanSantri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hafalan', models.CharField(max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('santri', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='santri.santri')),
            ],
        ),
        migrations.CreateModel(
            name='DokumentasiSantri',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', santri.compress_image.CompressedImageField(blank=True, default='no-image.png', help_text='format logo .jpg/.jpeg', null=True, quality=50, upload_to='santri')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('santri', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='santri.santri')),
            ],
        ),
    ]
