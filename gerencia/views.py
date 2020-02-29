from django.shortcuts import render
import datetime
from datetime import timedelta
from django.utils import timezone
import decimal
from decimal import Decimal
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from .models import clienteModel, subProdutoModel, produtoModel, orcamentoModel, produtoItemModel, caixaModel
from django.http import HttpResponse

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            now = now.hour
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 0 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 24:
                msgTelaInicial = "Boa Noite, " + request.user.get_short_name()
            return render (request, 'gerencia/home.html', {'title':'Home', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def clientesHome(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            now = now.hour
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
                
            return render (request, 'gerencia/cliente/clienteHome.html', {'title':'Clientes', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def clientesNovo(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            now = now.hour
            today = now
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == 'POST' and request.POST.get('nome') != None:
                nome = request.POST.get('nome')
                telefone = request.POST.get('telefone')
                email = request.POST.get('email')
                cnpj = request.POST.get('cnpj')
                cpf = request.POST.get('cpf')
                dataNascimento = request.POST.get('dataNascimento')
                celular = request.POST.get('celular')
                newCliente = clienteModel(nome=nome, telefone=telefone, email=email, cnpj=cnpj, cpf=cpf, dataNascimento=dataNascimento, celular=celular)
                newCliente.save()
                msgConfirmacao = "Cliente cadastrado com sucesso!"
                return render (request, 'gerencia/cliente/clienteNovo.html', {'title':'Novo Cliente', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'today':today,
                                                            'msgConfirmacao':msgConfirmacao})
            return render (request, 'gerencia/cliente/clienteNovo.html', {'title':'Novo Cliente', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'today':today})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def clientesBusca(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            now = now.hour
            clientesAtivos = clienteModel.objects.filter(estado=1).all().order_by('nome')
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
                
            return render (request, 'gerencia/cliente/clienteBusca.html', {'title':'Buscar Cliente', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'clientesAtivos':clientesAtivos})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def clientesVisualizar(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            now = now.hour
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == 'GET' and request.GET.get('clienteID') != None:
                clienteID = request.GET.get('clienteID')
                clienteObj = clienteModel.objects.filter(id=clienteID).get()
                return render (request, 'gerencia/cliente/clienteVisualizar.html', {'title':'Visualizar Cliente', 
                                                                            'msgTelaInicial':msgTelaInicial,
                                                                            'clienteObj':clienteObj})
                                                                            
            if request.method == 'POST' and request.POST.get('clienteID') != None:
                clienteID = request.POST.get('clienteID')
                clienteObj = clienteModel.objects.filter(id=clienteID).get()
                return render (request, 'gerencia/cliente/clienteVisualizar.html', {'title':'Visualizar Cliente', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'clienteObj':clienteObj})
            return render (request, 'gerencia/cliente/clienteVisualizar.html', {'title':'Visualizar Cliente', 
                                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def clientesEditar(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            now = now.hour
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == 'GET':
                clienteID = request.GET.get('clienteID')
                clienteObj = clienteModel.objects.filter(id=clienteID).get()
                return render (request, 'gerencia/cliente/clienteEditar.html', {'title':'Editar Cliente', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'clienteObj':clienteObj})
            if request.method == 'POST' and request.POST.get('clienteID') != None:
                clienteIDPost = request.POST.get('clienteID')
                clienteObj = clienteModel.objects.filter(id=clienteIDPost).get()

                nome = request.POST.get('nome')
                telefone = request.POST.get('telefone')
                email = request.POST.get('email')
                cnpj = request.POST.get('cnpj')
                cpf = request.POST.get('cpf')
                dataNascimento = request.POST.get('dataNascimento')
                celular = request.POST.get('celular')

                clienteObj.nome = nome 
                clienteObj.telefone = telefone
                clienteObj.email = email
                clienteObj.cnpj = cnpj
                clienteObj.cpf = cpf
                clienteObj.dataNascimento = dataNascimento
                clienteObj.celular = celular
                clienteObj.save()
                
                msgConfirmacao = "Cliente editado com sucesso!"
                return render (request, 'gerencia/cliente/clienteVisualizar.html', {'title':'Visualizar Cliente', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'clienteObj':clienteObj,
                                                                'msgConfirmacao':msgConfirmacao})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})
    
def produtosHome(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            now = now.hour
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
                
            return render (request, 'gerencia/produtoServico/produtoHome.html', {'title':'Produtos/Serviços', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})
    
def subProdutosNovo(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            now = now.hour
            today = now
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            subProdutosAtivos = subProdutoModel.objects.filter(estado=1).all().order_by('nome')
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == 'POST' and request.POST.get('nome') != None:
                nome = request.POST.get('nome')
                newSubProduto = subProdutoModel(nome=nome)
                newSubProduto.save()
                return render (request, 'gerencia/produtoServico/produtoNovo.html', {'title':'Novo Produto/Servico', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'today':today,
                                                            'subProdutosAtivos':subProdutosAtivos})
            return render (request, 'gerencia/produtoServico/produtoNovo.html', {'title':'Novo Produto/Servico', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'today':today,
                                                            'subProdutosAtivos':subProdutosAtivos})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def produtosNovo(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            now = now.hour
            today = now
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            subProdutosAtivos = subProdutoModel.objects.filter(estado=1).all().order_by('nome')
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == 'POST' and request.POST.get('nome') != None:
                subProduto = request.POST.get('subProduto')
                nome = request.POST.get('nome')
                unidade = request.POST.get('unidade')
                valor = request.POST.get('valor')
                prodserv = request.POST.get('prodserv')
                observacao = request.POST.get('observacao')
                subProdutoObj = subProdutoModel.objects.filter(id=subProduto).get()
                newProduto = produtoModel(subProduto=subProdutoObj, nome=nome, unidade=unidade, valor=valor, observacao=observacao)
                newProduto.save()
                msgConfirmacao = "Produto/Serviço cadastrado com sucesso!"
                return render (request, 'gerencia/produtoServico/produtoNovo.html', {'title':'Novo Produto/Servico', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'today':today,
                                                            'msgConfirmacao':msgConfirmacao,
                                                            'subProdutosAtivos':subProdutosAtivos})
            return render (request, 'gerencia/produtoServico/produtoNovo.html', {'title':'Novo Produto/Servico', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'today':today,
                                                            'subProdutosAtivos':subProdutosAtivos})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def produtosBusca(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            now = now.hour
            categorias = subProdutoModel.objects.filter(estado=1).all().order_by('nome')
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == 'POST' and request.POST.get('categoriaID') != None:
                categoriaID = request.POST.get('categoriaID')
                categoriaObj = subProdutoModel.objects.get(id=categoriaID)
                produtosAtivos = produtoModel.objects.filter(subProduto__id=categoriaObj.id, estado=1).all()
                subProdutoNome = categoriaObj.nome

                return render (request, 'gerencia/produtoServico/produtoBusca.html', {'title':'Buscar Produto/Serviço', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'produtosAtivos':produtosAtivos,
                                                                'subProdutoNome':subProdutoNome})
            
                
            return render (request, 'gerencia/produtoServico/produtoBusca.html', {'title':'Buscar Produto/Serviço', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'categorias':categorias})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def produtosVisualizar(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            now = now.hour
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == 'POST' and request.POST.get('produtoID') != None:
                produtoID = request.POST.get('produtoID')
                produtoObj = produtoModel.objects.filter(id=produtoID).get()
                return render (request, 'gerencia/produtoServico/produtoVisualizar.html', {'title':'Visualizar Produto/Serviço', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'produtoObj':produtoObj})
            return render (request, 'gerencia/produtoServico/produtoVisualizar.html', {'title':'Visualizar Produto/Serviço', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def produtosEditar(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            now = now.hour
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == 'GET':
                produtoID = request.GET.get('produtoID')
                produtoObj = produtoModel.objects.filter(id=produtoID).get()
                return render (request, 'gerencia/produtoServico/produtoEditar.html', {'title':'Editar Produto/Serviço', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'produtoObj':produtoObj})
            if request.method == 'POST' and request.POST.get('produtoID') != None:
                produtoID = request.POST.get('produtoID')
                subCategoria = request.POST.get('subCategoria')
                produtoObj = produtoModel.objects.filter(id=produtoID).get()
                for c in subProdutoModel.objects.all():
                    if c.nome == subCategoria:
                        produtoObj.subProduto = c
                    else:
                        novaCategoria = subProdutoModel(nome=subCategoria)
                        novaCategoria.save()
                        produtoObj.subProduto = novaCategoria

                nome = request.POST.get('nome')
                unidade = request.POST.get('unidade')
                valor = request.POST.get('novoValor')
                prodserv = request.POST.get('prodserv')
                observacao = request.POST.get('observacao')

                produtoObj.nome = nome 
                produtoObj.unidade = unidade
                if valor != None and valor != "":
                    produtoObj.valor = decimal.Decimal(valor)
                produtoObj.prodserv = prodserv
                produtoObj.observacao = observacao
                produtoObj.save()
                
                msgConfirmacao = "Produto/Serviço editado com sucesso!"
                return render (request, 'gerencia/produtoServico/produtoVisualizar.html', {'title':'Visualizar Produto/Serviço', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'produtoObj':produtoObj,
                                                                'msgConfirmacao':msgConfirmacao})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})
    
def orcamentosHome(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            now = now.hour
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
                
            return render (request, 'gerencia/orcamento/orcamentoHome.html', {'title':'Orçamentos', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})
    
def orcamentosNovo(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            now = now.hour
            today = now
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            clientesAtivos = clienteModel.objects.filter(estado=1).all().order_by('nome')
            produtosAtivos = produtoModel.objects.filter(estado=1).all().order_by('nome')
            subProdutosAtivos = subProdutoModel.objects.filter(estado=1).all().order_by('nome')

            try:
                orcamentoIDPost = request.POST.get('orcamentoID')
                orcamentoObjPost = orcamentoModel.objects.filter(id=orcamentoIDPost).get()
            except:
                orcamentoObjPost = None
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == 'GET' and request.GET.get('clienteID') != None:
                clienteIDGet = request.GET.get('clienteID')
                clienteObjto = clienteModel.objects.filter(id=clienteIDGet).get()
                return render (request, 'gerencia/orcamento/orcamentoNovo1.html', {'title':'Novo Orçamento', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'today':today,
                                                                'clienteObjto':clienteObjto,
                                                                'subProdutosAtivos':subProdutosAtivos})

            if request.method == 'POST' and request.POST.get('clienteID') != None and request.POST.get('orcamentoID') == None and request.POST.get('subProdutoID') != None:
                clienteIDPost = request.POST.get('clienteID')
                subProdutoIDPost = request.POST.get('subProdutoID')
                clienteObjto1 = clienteModel.objects.filter(id=clienteIDPost).get()
                subProdutoObj1 = subProdutoModel.objects.filter(id=subProdutoIDPost).get()
                produtosAtivos = produtoModel.objects.filter(subProduto__id=subProdutoIDPost, estado=1).all().order_by('nome')

                return render (request, 'gerencia/orcamento/orcamentoNovo1.html', {'title':'Novo Orçamento', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'today':today,
                                                            'clienteObjto':clienteObjto1,
                                                            'subProdutoNome':subProdutoObj1.nome,
                                                            'produtosAtivos':produtosAtivos})
            #IGOR
            if request.method == 'POST' and request.POST.get('clienteID') != None and request.POST.get('orcamentoID') == None and request.POST.get('produtoID') != None:
                clienteIDPost = request.POST.get('clienteID')
                clienteObj = clienteModel.objects.filter(id=clienteIDPost).get()
                orcamentoObjNew = orcamentoModel(cliente=clienteObj)
                orcamentoObjNew.save()
                produtoIDPost = request.POST.get('produtoID')
                qntProd = request.POST.get('qntProd')
                prodObj = produtoModel.objects.filter(id=produtoIDPost).get()
                prodVlrTotal = decimal.Decimal(prodObj.valor) * int(qntProd)
                prodItemObj = produtoItemModel(produto=prodObj, quantidade=qntProd, total=prodVlrTotal)
                prodItemObj.save()
                orcamentoObjNew.produtoItem.add(prodItemObj)
                orcamentoObjNew.total = decimal.Decimal(orcamentoObjNew.total) + decimal.Decimal(prodItemObj.total) 
                orcamentoObjNew.subtotal = orcamentoObjNew.total
                orcamentoObjNew.save()
                subProdutosAtivos = subProdutoModel.objects.filter(estado=1).all().order_by('nome')
                return render (request, 'gerencia/orcamento/orcamentoNovo1.html', {'title':'Novo Orçamento', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'today':today,
                                                            'orcamentoObj':orcamentoObjNew,
                                                            'subProdutosAtivos':subProdutosAtivos})
            if request.method == 'POST' and request.POST.get('orcamentoID') != None and request.POST.get('produtoID') == None and request.POST.get('subProdutoID') != None:
                orcamentoIDPost = request.POST.get('orcamentoID')
                orcamentoObjPost = orcamentoModel.objects.filter(id=orcamentoIDPost).get()
                subProdutoIDPost = request.POST.get('subProdutoID')
                subProdutoObj1 = subProdutoModel.objects.filter(id=subProdutoIDPost).get()
                produtosAtivos = produtoModel.objects.filter(subProduto__id=subProdutoIDPost, estado=1).all().order_by('nome')
                return render (request, 'gerencia/orcamento/orcamentoNovo1.html', {'title':'Novo Orçamento', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'today':today,
                                                            'orcamentoObj':orcamentoObjPost,
                                                            'subProdutoNome':subProdutoObj1.nome,
                                                            'produtosAtivos':produtosAtivos})
            if request.method == 'POST' and request.POST.get('orcamentoID') != None and request.POST.get('clienteID') == None and request.POST.get('subProdutoID') == None and request.POST.get('produtoID') == None:
                orcamentoIDPost = request.POST.get('orcamentoID')
                orcamentoObjPost = orcamentoModel.objects.filter(id=orcamentoIDPost).get()                
                subProdutosAtivos = subProdutoModel.objects.filter(estado=1).all().order_by('nome')

                return render (request, 'gerencia/orcamento/orcamentoNovo1.html', {'title':'Novo Orçamento', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'today':today,
                                                            'orcamentoObj':orcamentoObjPost,
                                                            'subProdutosAtivos':subProdutosAtivos})
            if request.method == 'POST' and request.POST.get('orcamentoID') != None and request.POST.get('subProdutoID') == None and request.POST.get('produtoID') != None:
                if request.POST.get('produtoID') != None and request.POST.get('produtoID') != "None": 
                    produtoIDPost = request.POST.get('produtoID')
                    qntProd = request.POST.get('qntProd')
                    prodObj = produtoModel.objects.filter(id=produtoIDPost).get()
                    prodVlrTotal = decimal.Decimal(prodObj.valor) * int(qntProd)
                    prodItemObj = produtoItemModel(produto=prodObj, quantidade=qntProd, total=prodVlrTotal)
                    prodItemObj.save()
                    orcamentoObjPost.produtoItem.add(prodItemObj)
                    orcamentoObjPost.total = orcamentoObjPost.total + prodItemObj.total 
                    orcamentoObjPost.subtotal = orcamentoObjPost.total
                orcamentoObjPost.save()
                
                return render (request, 'gerencia/orcamento/orcamentoNovo1.html', {'title':'Novo Orçamento', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'today':today,
                                                            'orcamentoObj':orcamentoObjPost})
            return render (request, 'gerencia/orcamento/orcamentoNovo.html', {'title':'Novo Orçamento', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'today':today,
                                                            'clientesAtivos':clientesAtivos})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})


def orcamentosBaixa(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            now = now.hour
            clientesAtivos = clienteModel.objects.filter(estado=1).all().order_by('nome')
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == 'GET' and request.GET.get('orcamentoID') != None and request.GET.get('clienteID') == None:
                orcamentoID = request.GET.get('orcamentoID')
                orcamentoObj = orcamentoModel.objects.filter(id=orcamentoID).get()
                return render (request, 'gerencia/orcamento/orcamentoBaixa1.html', {'title':'Baixa Orçamento', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'orcamentoObj':orcamentoObj})
            if request.method == 'GET' and request.GET.get('clienteID') != None:
                clienteID = request.GET.get('clienteID')
                orcamentosAll = orcamentoModel.objects.filter(cliente__id=clienteID).filter(estado=1).all().order_by('-dataCadastro')
                return render (request, 'gerencia/orcamento/orcamentoSelectVisualizarBaixa.html', {'title':'Baixa Orçamento', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'orcamentosAll':orcamentosAll})
                
            return render (request, 'gerencia/orcamento/orcamentosBaixa.html', {'title':'Baixa Orçamento', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'clientesAtivos':clientesAtivos})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def orcamentosBaixado(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            hora = now.hour
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if hora >= 4 and hora <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif hora > 11 and hora < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif hora >= 18 and hora < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == 'POST' and request.POST.get('orcamentoID') != None:
                orcamentoID = request.POST.get('orcamentoID')
                desconto = request.POST.get('desconto')
                metodo = request.POST.get('metodo')
                orcamentoObj = orcamentoModel.objects.filter(id=orcamentoID).get()
                if desconto != None  and desconto != "":
                    orcamentoObj.total = orcamentoObj.total - decimal.Decimal(desconto)
                    orcamentoObj.desconto = desconto
                orcamentoObj.metodo = metodo
                orcamentoObj.estado = 2
                orcamentoObj.dataFechamento = now
                orcamentoObj.save()
                try:
                    lastCaixa = caixaModel.objects.latest('id')
                except:
                    lastCaixa = caixaModel(total=0)
                    lastCaixa.save()
                totalCaixa = decimal.Decimal(lastCaixa.total) + decimal.Decimal(orcamentoObj.total) 
                lastCaixa.pagamento = metodo
                if desconto != None  and desconto != "":
                    lastCaixa.desconto = desconto
                lastCaixa.valorOperacao = decimal.Decimal(orcamentoObj.total) 
                lastCaixa.total = totalCaixa
                lastCaixa.referencia = orcamentoObj.id 
                lastCaixa.save()

                msgConfirmacao = "Orçamento baixado com sucesso!"
                return render (request, 'gerencia/orcamento/orcamentoHome.html', {'title':'Orçamentos', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'msgConfirmacao':msgConfirmacao,
                                                                'orcamentoObj':orcamentoObj})
            return render (request, 'gerencia/orcamento/orcamentosBaixa.html', {'title':'Baixar Orçamento', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def orcamentosBusca(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            hora = now.hour
            clientesAtivos = clienteModel.objects.filter(estado=1).all().order_by('nome')
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if hora >= 4 and hora <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif hora > 11 and hora < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif hora >= 18 and hora < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == 'GET' and request.GET.get('orcamentoID') != None and request.GET.get('clienteID') == None:
                orcamentoID = request.GET.get('orcamentoID')
                orcamentoObj = orcamentoModel.objects.filter(id=orcamentoID).get()
                return render (request, 'gerencia/orcamento/orcamentoVisualizar.html', {'title':'Visualizar Orçamento', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'orcamentoObj':orcamentoObj})
            if request.method == 'GET' and request.GET.get('clienteID') != None:
                clienteID = request.GET.get('clienteID')
                orcamentosAll = orcamentoModel.objects.filter(cliente__id=clienteID).all().order_by('-dataCadastro')
                return render (request, 'gerencia/orcamento/orcamentoSelectVisualizar.html', {'title':'Visualizar Orçamento', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'orcamentosAll':orcamentosAll})
                
            return render (request, 'gerencia/orcamento/orcamentoBusca.html', {'title':'Buscar Orçamento', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'clientesAtivos':clientesAtivos})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def orcamentosVisualizar(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            now = now.hour
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == 'GET' and request.GET.get('orcamentoID') != None:
                orcamentoID = request.GET.get('orcamentoID')
                orcamentoObj = orcamentoModel.objects.filter(id=orcamentoID).get()
                return render (request, 'gerencia/orcamento/orcamentoVisualizar.html', {'title':'Visualizar Orçamento', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'orcamentoObj':orcamentoObj})
            return render (request, 'gerencia/orcamento/orcamentoVisualizar.html', {'title':'Visualizar Orçamento', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def orcamentosEditar(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            now = now.hour
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == 'GET':
                produtoID = request.GET.get('produtoID')
                produtoObj = produtoModel.objects.filter(id=produtoID).get()
                return render (request, 'gerencia/orcamento/orcamentoEditar.html', {'title':'Editar Orçamento', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'produtoObj':produtoObj})
            if request.method == 'POST' and request.POST.get('produtoID') != None:
                produtoID = request.POST.get('produtoID')
                produtoObj = produtoModel.objects.filter(id=produtoID).get()

                nome = request.POST.get('nome')
                unidade = request.POST.get('unidade')
                valor = request.POST.get('valor')
                prodserv = request.POST.get('prodserv')
                observacao = request.POST.get('observacao')

                produtoObj.nome = nome 
                produtoObj.unidade = unidade
                produtoObj.valor = valor
                produtoObj.prodserv = prodserv
                produtoObj.observacao = observacao
                produtoObj.save()
                
                msgConfirmacao = "Produto/Serviço editado com sucesso!"
                return render (request, 'gerencia/orcamento/orcamentoVisualizar.html', {'title':'Visualizar Orçamento', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'produtoObj':produtoObj,
                                                                'msgConfirmacao':msgConfirmacao})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def orcamentosExcluirItem(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            hora = now.hour
            today = now
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if hora >= 4 and hora <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif hora > 11 and hora < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif hora >= 18 and hora < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == 'POST' and request.POST.get('prodItemIDNovo') != None and request.POST.get('orcamentoID') != None:
                orcamentoID = request.POST.get('orcamentoID')
                orcamentoObj = orcamentoModel.objects.filter(id=orcamentoID).get()
                prodItemID = request.POST.get('prodItemIDNovo')
                prodItemObj = produtoItemModel.objects.filter(id=prodItemID).get()
                orcamentoObj.produtoItem.remove(prodItemObj)
                orcamentoObj.total = orcamentoObj.total - decimal.Decimal(prodItemObj.total) 
                orcamentoObj.subtotal = orcamentoObj.total
                orcamentoObj.save()
                subProdutosAtivos = subProdutoModel.objects.filter(estado=1).all().order_by('nome')
                return render (request, 'gerencia/orcamento/orcamentoNovo1.html', {'title':'Novo/Editar Orçamento', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'today':today,
                                                            'orcamentoObj':orcamentoObj,
                                                            'subProdutosAtivos':subProdutosAtivos})
            
            return render (request, 'gerencia/orcamento/orcamentoVisualizar.html', {'title':'Visualizar Orçamento', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})
    
def caixaHome(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            now = now.hour
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
                
            return render (request, 'gerencia/caixa/caixaHome.html', {'title':'Caixa', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})
    
def caixaEntrada(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            hora = now.hour
            mes = now.month
            today = now
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if hora >= 4 and hora <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif hora > 11 and hora < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif hora >= 18 and hora < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            try:
                lastCaixa = caixaModel.objects.latest('id')
            except:
                lastCaixa = caixaModel(total=0)
                lastCaixa.save()
            try:
                lastCaixa = caixaModel.objects.latest('id')
            except:
                lastCaixa = caixaModel(total=0)
                lastCaixa.save()
            if request.method == 'POST' and request.POST.get('valorOperacao') != None:        
                pagamento = request.POST.get('pagamento')     
                descricao = request.POST.get('descricao')     
                valorOperacao = request.POST.get('valorOperacao')
                novoTotal = lastCaixa.total + decimal.Decimal(valorOperacao)
                caixaNovo = caixaModel(operacao=1, total=novoTotal, pagamento=pagamento, referencia="Entrada", descricao=descricao, valorOperacao=valorOperacao)
                caixaNovo.save()
                msgConfirmacao = "Entrada efetuada com sucesso!"
                caixaAll = caixaModel.objects.filter(dataCadastro__month=mes).all().order_by('-dataCadastro')
                lastCaixa = caixaModel.objects.latest('id')
                return render (request, 'gerencia/caixa/caixaBalanco.html', {'title':'Balanço', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'caixaObj':lastCaixa,
                                                            'caixaAll':caixaAll,
                                                            'msgConfirmacao':msgConfirmacao,
                                                            'today':today})
                
            return render (request, 'gerencia/caixa/caixaEntrada.html', {'title':'Entrada', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'caixaObj':lastCaixa})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})
    
def caixaSaida(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            hora = now.hour
            mes = now.month
            today = now
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if hora >= 4 and hora <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif hora > 11 and hora < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif hora >= 18 and hora < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            try:
                lastCaixa = caixaModel.objects.latest('id')
            except:
                lastCaixa = caixaModel(total=0)
                lastCaixa.save()
            if request.method == 'POST' and request.POST.get('valorOperacao') != None:        
                pagamento = request.POST.get('pagamento')     
                descricao = request.POST.get('descricao')     
                valorOperacao = request.POST.get('valorOperacao')
                novoTotal = lastCaixa.total - decimal.Decimal(valorOperacao)
                caixaNovo = caixaModel(operacao=2, total=novoTotal, pagamento=pagamento, referencia="Retirada", descricao=descricao, valorOperacao=valorOperacao)
                caixaNovo.save()
                msgConfirmacao = "Retirada efetuada com sucesso!"
                caixaAll = caixaModel.objects.filter(dataCadastro__month=mes).all().order_by('-dataCadastro')
                lastCaixa = caixaModel.objects.latest('id')
                return render (request, 'gerencia/caixa/caixaBalanco.html', {'title':'Balanço', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'caixaObj':lastCaixa,
                                                            'caixaAll':caixaAll,
                                                            'msgConfirmacao':msgConfirmacao,
                                                            'today':today})

            return render (request, 'gerencia/caixa/caixaSaida.html', {'title':'Saída', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'caixaObj':lastCaixa})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})
    
def caixaBalanco(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            mes = now.month
            hora = now.hour
            dataFim = now
            dataInicio = now + timezone.timedelta(days=-30)
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if hora >= 4 and hora <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif hora > 11 and hora < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif hora >= 18 and hora < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            try:
                lastCaixa = caixaModel.objects.latest('id')
            except:
                lastCaixa = caixaModel(total=0)
                lastCaixa.save()
            caixaAll = caixaModel.objects.filter(dataCadastro__range=(dataInicio,dataFim)).all().order_by('-dataCadastro')
            lastCaixa = caixaModel.objects.latest('id')
            if request.method == 'POST' and request.POST.get('dataInicio') != None and request.POST.get('dataFim') != None:
                dataInicio = request.POST.get('dataInicio')
                dataFim = request.POST.get('dataFim')
                caixaAll = caixaModel.objects.filter(dataCadastro__range=(dataInicio,dataFim)).all().order_by('-dataCadastro')
                dataInicio = datetime.datetime.strptime(dataInicio, "%Y-%m-%d").date()
                dataFim = datetime.datetime.strptime(dataFim, "%Y-%m-%d").date()
                return render (request, 'gerencia/caixa/caixaBalanco.html', {'title':'Balanço', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'caixaObj':lastCaixa,
                                                            'dataInicio':dataInicio,
                                                            'dataFim':dataFim,
                                                            'caixaAll':caixaAll})
            return render (request, 'gerencia/caixa/caixaBalanco.html', {'title':'Balanço', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'caixaObj':lastCaixa,
                                                            'dataInicio':dataInicio,
                                                            'dataFim':dataFim,
                                                            'caixaAll':caixaAll})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})