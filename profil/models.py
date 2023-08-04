from django.db import models
from santri.compress_image import CompressedImageField

# Create your models here.

class ProfilWalikelas(models.Model):
    nama_guru = models.CharField(max_length=100)
    niy = models.CharField(max_length=100, blank=True, null=True)
    jabatan = models.CharField(max_length=100)
    no_hp = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    pendidikan = models.CharField(max_length=150)
    foto = CompressedImageField(upload_to='ustadz', default='no-image.png', blank=True, null=True, quality=50,
                                help_text="format logo .jpg/.jpeg")

    def __str__(self):
        return self.nama_guru