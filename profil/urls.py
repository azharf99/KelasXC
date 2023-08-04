from django.urls import path
from profil.views import ProfilIndexView

urlpatterns = [
    path('', ProfilIndexView.as_view(), name="profil-index"),
]