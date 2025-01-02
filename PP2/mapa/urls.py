from django.urls import path
from . import views  # Importa as views do app

urlpatterns = [
    # Exemplo de configuração de uma view chamada `home`
    path('', views.home, name='home'),
    path('teste', views.teste, name='teste'),
    
]
