from django.contrib import admin
from santri.models import (Santri, PelanggaranSantri, DokumentasiSantri, HafalanSantri,
                           PrestasiSantri, DokumentasiKelas, PrestasiKelas)

# Register your models here.

admin.site.register(Santri)
admin.site.register(PrestasiSantri)
admin.site.register(HafalanSantri)
admin.site.register(DokumentasiSantri)
admin.site.register(PelanggaranSantri)
admin.site.register(PrestasiKelas)
admin.site.register(DokumentasiKelas)
