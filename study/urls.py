from django.urls import path, re_path, register_converter
from . import views


urlpatterns = [
    path('', views.study, name='study'),  # http://127.0.0.1:8000
    re_path(r'archive/(?P<year>[0-9]{4})/', views.archive)
]
