from django.shortcuts import render
import datetime
import decimal
from django.contrib.auth.models import User
from django.utils.crypto import get_random_string
from .models import clienteModel, produtoModel, orcamentoModel, produtoItemModel
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
    
def produtosNovo(request):
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
                unidade = request.POST.get('unidade')
                valor = request.POST.get('valor')
                prodserv = request.POST.get('prodserv')
                observacao = request.POST.get('observacao')
                newProduto = produtoModel(nome=nome, unidade=unidade, valor=valor, prodserv=prodserv, observacao=observacao)
                newProduto.save()
                msgConfirmacao = "Produto/Serviço cadastrado com sucesso!"
                return render (request, 'gerencia/produtoServico/produtoNovo.html', {'title':'Novo Produto/Servico', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'today':today,
                                                            'msgConfirmacao':msgConfirmacao})
            return render (request, 'gerencia/produtoServico/produtoNovo.html', {'title':'Novo Produto/Servico', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'today':today})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def produtosBusca(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            now = now.hour
            produtosAtivos = produtoModel.objects.filter(estado=1, prodserv=1).all().order_by('nome')
            servicosAtivos = produtoModel.objects.filter(estado=1, prodserv=2).all().order_by('nome')
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
                
            return render (request, 'gerencia/produtoServico/produtoBusca.html', {'title':'Buscar Produto/Serviço', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'produtosAtivos':produtosAtivos,
                                                            'servicosAtivos':servicosAtivos})
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
            produtosAtivos = produtoModel.objects.filter(prodserv=1).all().order_by('nome')
            servicosAtivos = produtoModel.objects.filter(prodserv=2).all().order_by('nome')
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
                                                            'produtosAtivos':produtosAtivos,
                                                            'servicosAtivos':servicosAtivos})

            if request.method == 'POST' and request.POST.get('clienteID') != None and orcamentoObjPost == None:
                clienteIDPost = request.POST.get('clienteID')
                clienteObj = clienteModel.objects.filter(id=clienteIDPost).get()
                orcamentoObjNew = orcamentoModel(cliente=clienteObj)
                orcamentoObjNew.save()
                if request.POST.get('produtoID') != None: 
                    produtoIDPost = request.POST.get('produtoID')
                    qntProd = request.POST.get('qntProd')
                    prodObj = produtoModel.objects.filter(id=produtoIDPost).get()
                    prodVlrTotal = decimal.Decimal(prodObj.valor) * int(qntProd)
                    prodItemObj = produtoItemModel(produto=prodObj, quantidade=qntProd, total=prodVlrTotal)
                    prodItemObj.save()
                    orcamentoObjNew.produtoItem.add(prodItemObj)
                    orcamentoObjNew.total = decimal.Decimal(orcamentoObjNew.total) + decimal.Decimal(prodItemObj.total) 
                if request.POST.get('servicoID') != None:
                    servicoIDPost = request.POST.get('servicoID')
                    qntServ = request.POST.get('qntServ')
                    servObj = produtoModel.objects.filter(id=servicoIDPost).get()
                    serVlrTotal = decimal.Decimal(servObj.valor) * int(qntServ)
                    servItemObj = produtoItemModel(produto=servObj, quantidade=qntServ, total=serVlrTotal)
                    servItemObj.save()
                    orcamentoObjNew.produtoItem.add(servItemObj)
                    orcamentoObjNew.total = decimal.Decimal(orcamentoObjNew.total) + decimal.Decimal(servItemObj.total) 
                orcamentoObjNew.save()
                return render (request, 'gerencia/orcamento/orcamentoNovo1.html', {'title':'Novo Orçamento', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'today':today,
                                                            'orcamentoObj':orcamentoObjNew,
                                                            'produtosAtivos':produtosAtivos,
                                                            'servicosAtivos':servicosAtivos})
            if request.method == 'POST' and orcamentoObjPost != None:
                if request.POST.get('produtoID') != None: 
                    produtoIDPost = request.POST.get('produtoID')
                    qntProd = request.POST.get('qntProd')
                    prodObj = produtoModel.objects.filter(id=produtoIDPost).get()
                    prodVlrTotal = decimal.Decimal(prodObj.valor) * int(qntProd)
                    prodItemObj = produtoItemModel(produto=prodObj, quantidade=qntProd, total=prodVlrTotal)
                    prodItemObj.save()
                    orcamentoObjPost.produtoItem.add(prodItemObj)
                    orcamentoObjPost.total = orcamentoObjPost.total + prodItemObj.total 
                if request.POST.get('servicoID') != None:
                    servicoIDPost = request.POST.get('servicoID')
                    qntServ = request.POST.get('qntServ')
                    servObj = produtoModel.objects.filter(id=servicoIDPost).get()
                    serVlrTotal = decimal.Decimal(servObj.valor) * int(qntServ)
                    servItemObj = produtoItemModel(produto=servObj, quantidade=qntServ, total=serVlrTotal)
                    servItemObj.save()
                    orcamentoObjPost.produtoItem.add(servItemObj)
                    orcamentoObjPost.total = orcamentoObjPost.total + servItemObj.total 
                orcamentoObjPost.save()
                return render (request, 'gerencia/orcamento/orcamentoNovo1.html', {'title':'Novo Orçamento', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'today':today,
                                                            'orcamentoObj':orcamentoObjPost,
                                                            'produtosAtivos':produtosAtivos,
                                                            'servicosAtivos':servicosAtivos})
            return render (request, 'gerencia/orcamento/orcamentoNovo.html', {'title':'Novo Orçamento', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'today':today,
                                                            'clientesAtivos':clientesAtivos})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})

def orcamentosBusca(request):
    if request.user.is_authenticated:
        if request.user.last_name == "GERENCIA":
            now = datetime.datetime.now()
            now = now.hour
            clientesAtivos = clienteModel.objects.filter(estado=1).all().order_by('nome')
            produtosAtivos = produtoModel.objects.filter(estado=1, prodserv=1).all().order_by('nome')
            servicosAtivos = produtoModel.objects.filter(estado=1, prodserv=2).all().order_by('nome')
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
            if request.method == 'GET' and request.GET.get('clienteID') != None:
                clienteID = request.GET.get('clienteID')
                orcamentosAll = orcamentoModel.objects.filter(cliente__id=clienteID).all().order_by('dataCadastro')
                return render (request, 'gerencia/orcamento/orcamentoSelectVisualizar.html', {'title':'Visualizar Orçamento', 
                                                                'msgTelaInicial':msgTelaInicial,
                                                                'orcamentosAll':orcamentosAll})
                
            return render (request, 'gerencia/orcamento/orcamentoBusca.html', {'title':'Buscar Orçamento', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'clientesAtivos':clientesAtivos,
                                                            'produtosAtivos':produtosAtivos,
                                                            'servicosAtivos':servicosAtivos})
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
            now = now.hour
            today = now
            msgTelaInicial = "Olá, " + request.user.get_short_name() 
            if now >= 4 and now <= 11:
                msgTelaInicial = "Bom dia, " + request.user.get_short_name() 
            elif now > 11 and now < 18:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name() 
            elif now >= 18 and now < 4:
                msgTelaInicial = "Boa Tarde, " + request.user.get_short_name()
            if request.method == 'POST' and request.POST.get('prodItemIDNovo') != None and request.POST.get('orcamentoID') != None:
                orcamentoID = request.POST.get('orcamentoID')
                orcamentoObj = orcamentoModel.objects.filter(id=orcamentoID).get()
                prodItemID = request.POST.get('prodItemIDNovo')
                prodItemObj = produtoItemModel.objects.filter(id=prodItemID).get()
                orcamentoObj.produtoItem.remove(prodItemObj)
                orcamentoObj.total = orcamentoObj.total - decimal.Decimal(prodItemObj.total) 
                orcamentoObj.save()
                produtosAtivos = produtoModel.objects.filter(prodserv=1).all().order_by('nome')
                servicosAtivos = produtoModel.objects.filter(prodserv=2).all().order_by('nome')
                return render (request, 'gerencia/orcamento/orcamentoNovo1.html', {'title':'Novo/Editar Orçamento', 
                                                            'msgTelaInicial':msgTelaInicial,
                                                            'today':today,
                                                            'orcamentoObj':orcamentoObj,
                                                            'produtosAtivos':produtosAtivos,
                                                            'servicosAtivos':servicosAtivos})
            
            return render (request, 'gerencia/orcamento/orcamentoVisualizar.html', {'title':'Visualizar Orçamento', 
                                                            'msgTelaInicial':msgTelaInicial})
        return render (request, 'site/login.html', {'title':'Login'})
    return render (request, 'site/login.html', {'title':'Login'})