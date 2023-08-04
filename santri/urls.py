from django.urls import path
from santri.views import (DokumentasiKelasView,
                          SantriIndexView, SantriDetailView, PrestasiKelasView)

urlpatterns = [
    path('', SantriIndexView.as_view(), name="santri-index"),
    path('<int:pk>', SantriDetailView.as_view(), name="santri-detail"),
    path('kelas/', DokumentasiKelasView.as_view(), name="kelas"),
    path('prestasi-kelas/', PrestasiKelasView.as_view(), name="prestasi-kelas"),
]