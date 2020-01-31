from django.db import models
from django.utils import timezone

# Create your models here.


class clienteModel(models.Model):
    ST = (
        ('1', 'Ativo'),
        ('2', 'Inativo'),
        ('3', 'Excluido'),
    )
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=1, choices=ST, default=1)
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15, null=True, blank=True)
    cnpj = models.CharField(max_length=30, null=True, blank=True)
    cpf = models.CharField(max_length=30, null=True, blank=True)
    dataNascimento = models.DateTimeField(
        default=timezone.now, null=True, blank=True)
    celular = models.CharField(max_length=15, null=True, blank=True)
    email = models.CharField(max_length=300, null=True, blank=True)
    dataCadastro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome


class produtoModel(models.Model):
    ST = (
        ('1', 'Ativo'),
        ('2', 'Inativo'),
        ('3', 'Excluido'),
    )
    PS = (
        ('1', 'Produto'),
        ('2', 'Serviço'),
    )
    UN = (
        ('1', 'N/A'),
        ('2', 'Metro'),
        ('3', 'Unidade'),
        ('4', 'Hora'),
        ('5', 'Dia'),
    )
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=1, choices=ST, default=1)
    prodserv = models.CharField(max_length=1, choices=PS, default=1)
    unidade = models.CharField(max_length=1, choices=PS, default=1)
    nome = models.CharField(max_length=200)
    observacao = models.CharField(max_length=200, null=True, blank=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    dataCadastro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome


class produtoItemModel(models.Model):
    id = models.AutoField(primary_key=True)
    produto = models.ForeignKey(produtoModel, on_delete=models.CASCADE)
    quantidade = models.CharField(max_length=15, default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    data_cadastro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.produto.nome


class orcamentoModel(models.Model):
    ES = (
        ('1', 'Aberto'),
        ('2', 'Finalizado'),
        ('3', 'Cancelado'),
        ('4', 'Descartado'),
    )
    PG = (
        ('1', 'Dinheiro'),
        ('2', 'Cartão'),
    )
    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=1, choices=ES, default=1)
    pagamento = models.CharField(max_length=1, choices=PG, null=True, blank=True)
    produtoItem = models.ManyToManyField(produtoItemModel)
    cliente = models.ForeignKey(clienteModel, on_delete=models.CASCADE)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    obs = models.CharField(max_length=1000, null=True, blank=True)
    dataFechamento = models.DateTimeField(default=timezone.now)
    dataCadastro = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.cliente.nome


class caixaModel(models.Model):
    OP = (
        ('1', 'Entrada'),
        ('2', 'Saida'),
    )
    PG = (
        ('1', 'Dinheiro'),
        ('2', 'Cartao'),
    )
    id = models.AutoField(primary_key=True)
    operacao = models.CharField(max_length=1, choices=OP, default=1)
    total = models.DecimalField(max_digits=10, decimal_places=2)    
    pagamento = models.CharField(max_length=1, choices=PG, null=True, blank=True)
    referencia = models.CharField(max_length=200, null=True, blank=True)
    descricao = models.CharField(max_length=200, null=True, blank=True)
    desconto = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    valorOperacao = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    dataCadastro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.str(id)
