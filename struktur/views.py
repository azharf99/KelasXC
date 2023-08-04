from django.shortcuts import render
from django.views.generic import ListView
from struktur.models import StrukturKelas

# Create your views here.

class StrukturIndexView(ListView):
    model = StrukturKelas