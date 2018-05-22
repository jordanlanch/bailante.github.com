from django.urls import path
from estudiantes.views import (
   HomeView
)

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
]
