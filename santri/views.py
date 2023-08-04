from django.shortcuts import render
from django.views.generic import ListView, DetailView
from santri.models import (Santri, PelanggaranSantri, DokumentasiSantri,
                           HafalanSantri, PrestasiSantri, DokumentasiKelas, PrestasiKelas)
# Create your views here.

class SantriIndexView(ListView):
    model = Santri
    paginate_by = 10


class SantriDetailView(DetailView):
    model = Santri

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['prestasi'] = PrestasiSantri.objects.filter(santri_id=self.kwargs.get('pk'))
        context['pelanggaran'] = PelanggaranSantri.objects.filter(santri_id=self.kwargs.get('pk'))
        context['hafalan'] = HafalanSantri.objects.filter(santri_id=self.kwargs.get('pk'))
        context['dokumentasi'] = DokumentasiSantri.objects.filter(santri_id=self.kwargs.get('pk'))

        return context

class DokumentasiKelasView(ListView):
    model = DokumentasiKelas


class PrestasiKelasView(ListView):
    model = PrestasiKelas