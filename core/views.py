from django.shortcuts import render, redirect
from .models import Carro
from .forms import CarroForm


# Create your views here.
def index(request):
    carros = Carro.objects.all()
    contexto = {
        'carros': carros
    }
    return render(request,'core/index.html',contexto)

def lista(request):
    carros = Carro.objects.all()
    contexto = {
        'carros': carros
    }
    return render(request,'core/lista.html',contexto)


def cadastro(request):
    form = CarroForm()
    if request.method == 'POST':
        form = CarroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_carro')
        
        form = CarroForm()
    contexto={
             'form': form
    }  
    return render(request,'core/form.html',contexto)

def editar_carro(request,id):
    carro = Carro.objects.get(id=id)

    if request.method == 'POST':
        form = CarroForm(request.POST,instance=carro)
        if form.is_valid():
            form.save()
            return redirect('lista_carro')
    else:
        form = CarroForm(instance=carro)

    contexto={
            'form':form
    }
    return render(request,'core/form.html',contexto)
        
def remover_carro(request,id):
    carro = Carro.objects.get(id=id)
    carro.delete()
    return redirect('lista_carro')

    

