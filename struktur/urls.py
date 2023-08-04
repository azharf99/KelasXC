from django.urls import path
from struktur.views import StrukturIndexView

urlpatterns = [
    path('', StrukturIndexView.as_view(), name="struktur-index"),
]