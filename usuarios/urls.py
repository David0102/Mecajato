from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('home/', views.home, name='home'),
    path('logout/', views.logout_user, name='logout')
]