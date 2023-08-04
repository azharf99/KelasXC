from django.shortcuts import render
from django.views.generic import ListView
from profil.models import ProfilWalikelas
# Create your views here.

class ProfilIndexView(ListView):
    model = ProfilWalikelas
