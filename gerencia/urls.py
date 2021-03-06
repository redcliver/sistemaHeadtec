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
    url(r'subProdutosNovo/', views.subProdutosNovo),
    url(r'produtosNovo/', views.produtosNovo),
    url(r'produtosBusca/', views.produtosBusca),
    url(r'produtosVisualizar/', views.produtosVisualizar),
    url(r'produtosEditar/', views.produtosEditar),
    url(r'orcamentosHome/', views.orcamentosHome),
    url(r'^orcamentosNovo/', views.orcamentosNovo),
    url(r'^orcamentosBaixa/', views.orcamentosBaixa),
    url(r'^orcamentosBaixado/', views.orcamentosBaixado),
    url(r'orcamentosBusca/', views.orcamentosBusca),
    url(r'orcamentosVisualizar/', views.orcamentosVisualizar),
    url(r'orcamentosEditar/', views.orcamentosEditar),
    url(r'orcamentosExcluirItem/', views.orcamentosExcluirItem),
    url(r'caixaHome/', views.caixaHome),
    url(r'caixaEntrada/', views.caixaEntrada),
    url(r'caixaSaida/', views.caixaSaida),
    url(r'caixaBalanco/', views.caixaBalanco),
]
