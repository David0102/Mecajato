from django.urls import path
from . import views

urlpatterns = [
    path('', views.servicos, name="servicos"),
    path('lista_servicos/', views.lista_servicos, name="lista_servicos"),
    path('servico/<str:identificador>', views.servico, name="servico"),
    path('gerar_os/<str:identificador>', views.gerar_os, name="gerar_os")
]