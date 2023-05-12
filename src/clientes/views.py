from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Cliente, Carro
import re
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.shortcuts import redirect, get_object_or_404

def clientes(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            clientes_list = Cliente.objects.all()
            return render(request, 'clientes.html', {'clientes': clientes_list})
        else:
            return redirect(reverse('login'))
    
    elif request.method == "POST":
        nome = request.POST.get('nome')
        sobrenome = request.POST.get('sobrenome')
        email = request.POST.get('email')
        cpf = request.POST.get('cpf')
        carros = request.POST.getlist('carro')
        placas = request.POST.getlist('placa')
        anos = request.POST.getlist('ano')

        cliente = Cliente.objects.filter(cpf = cpf)
        
        if cliente.exists():
            return render(request, 'clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'email': email, 'carros': zip(carros, placas, anos)})
        
        if not re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$", email):
            return render(request, 'clientes.html', {'nome': nome, 'sobrenome': sobrenome, 'cpf': cpf, 'carros': zip(carros, placas, anos)})

        cliente = Cliente(
            nome = nome,
            sobrenome = sobrenome, 
            email = email,
            cpf = cpf
        )

        cliente.save()

        for carro, placa, ano in zip(carros, placas, anos):
            car = Carro(carro = carro, placa = placa, ano = ano, cliente = cliente)
            car.save()

        return redirect(reverse('clientes'))

    

def att_cliente(request):
    id_cliente = request.POST.get('id_cliente')

    cliente = Cliente.objects.filter(id=id_cliente)
    carros  = Carro.objects.filter(cliente = cliente[0])


    cliente_json = json.loads(serializers.serialize('json', cliente))[0]['fields']
    cliente_id = json.loads(serializers.serialize('json', cliente))[0]['pk']
    carros_json = json.loads(serializers.serialize('json', carros))
    carros_json = [{'fields': carro['fields'], 'id': carro['pk']} for carro in carros_json]

    data = {'cliente': cliente_json, 'carros': carros_json, 'cliente_id': cliente_id}
    return JsonResponse(data)

@csrf_exempt
def update_carro(request, id):
    nome_carro = request.POST.get('carro')
    placa_carro = request.POST.get('placa')
    ano_carro = request.POST.get('ano')

    carro = Carro.objects.get(id=id)
    list_carros = Carro.objects.exclude(id=id).filter(placa=placa_carro)

    if list_carros.exists():
        return HttpResponse('Placa já existente!')
    
    carro.carro = nome_carro
    carro.placa = placa_carro
    carro.ano = ano_carro
    carro.save()
    return HttpResponse('Dados alterados!')

def excluir_carro(request, id):
    try:
        carro = Carro.objects.get(id=id)
        carro.delete()
        return redirect(reverse('clientes')+f'?aba=att_cliente&id_cliente={id}')
    except:
        return redirect(reverse('clientes'))

def update_cliente(request, id):
    body = json.loads(request.body)
    
    nome = body['nome']
    sobrenome = body['sobrenome']
    email = body['email']
    cpf = body['cpf']

    cliente = get_object_or_404(Cliente, id=id)
    list_cliente = Cliente.objects.exclude(id=id).filter(cpf=cpf)

    if list_cliente.exists():
        return JsonResponse({'status': 'erro1'})
    
    if not re.search(r"^[A-Za-z0-9_!#$%&'*+\/=?`{|}~^.-]+@[A-Za-z0-9.-]+$", email):
        return JsonResponse({'status': 'erro2'})

    try:
        cliente.nome = nome
        cliente.sobrenome = sobrenome
        cliente.email = email
        cliente.cpf = cpf
        cliente.save()
        return JsonResponse({'status': '200', 'nome': nome, 'sobrenome': sobrenome, 'email': email, 'cpf': cpf})
    except:
        return JsonResponse({'status': '500'})


def excluir_cliente(request):
    id = request.POST.get('id')

    try:
        cliente = Cliente.objects.get(id=id)
        cliente.delete()
        return JsonResponse({'status': 'ok'})
    except:
        return JsonResponse({'status': 'erro'})