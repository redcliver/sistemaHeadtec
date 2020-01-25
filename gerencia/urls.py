from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home),
    url(r'clientesHome/', views.clientesHome),
    url(r'clientesNovo/', views.clientesNovo),
    url(r'clientesBusca/', views.clientesBusca),
    url(r'clientesVisualizar/', views.clientesVisualizar),
    url(r'clientesEditar/', views.clientesEditar),
    url(r'produtosHome/', views.produtosHome),
    url(r'produtosNovo/', views.produtosNovo),
    url(r'produtosBusca/', views.produtosBusca),
    url(r'produtosVisualizar/', views.produtosVisualizar),
    url(r'produtosEditar/', views.produtosEditar),
]