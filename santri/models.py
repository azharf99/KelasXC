from django.db import models
from santri.compress_image import CompressedImageField

# Create your models here.

class DokumentasiKelas(models.Model):
    foto = CompressedImageField(upload_to='kelas', default='no-image.png', blank=True, null=True, quality=50, help_text="format logo .jpg/.jpeg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Foto kelas tangal{self.created_at}"

class PrestasiKelas(models.Model):
    prestasi = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.prestasi

class Santri(models.Model):
    nama_santri = models.CharField(max_length=100)
    nis = models.CharField(max_length=100)
    tempat_lahir = models.CharField(max_length=100, blank=True, null=True)
    tanggal_lahir = models.DateField(blank=True, null=True)
    alamat = models.CharField(max_length=200, blank=True, null=True)
    foto = CompressedImageField(upload_to='kelas', default='no-image.png', blank=True, null=True, quality=50,
                                help_text="format logo .jpg/.jpeg")

    def __str__(self):
        return self.nama_santri

class DokumentasiSantri(models.Model):
    santri = models.ForeignKey(Santri, on_delete=models.CASCADE)
    foto = CompressedImageField(upload_to='santri', default='no-image.png', blank=True, null=True, quality=50, help_text="format logo .jpg/.jpeg")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.santri


class PelanggaranSantri(models.Model):
    santri = models.ForeignKey(Santri, on_delete=models.CASCADE)
    pelanggaran = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.santri} | {self.pelanggaran}"


class PrestasiSantri(models.Model):
    santri = models.ForeignKey(Santri, on_delete=models.CASCADE)
    prestasi = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.santri} | {self.prestasi}"


class HafalanSantri(models.Model):
    santri = models.ForeignKey(Santri, on_delete=models.CASCADE)
    hafalan = models.CharField(max_length=200)
    catatan = models.CharField(max_length=200, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.santri} | {self.hafalan}"