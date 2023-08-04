from django.db import models
from santri.models import Santri
# Create your models here.

class StrukturKelas(models.Model):
    santri = models.ForeignKey(Santri, on_delete=models.CASCADE)
    jabatan = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.santri} ({self.jabatan})"