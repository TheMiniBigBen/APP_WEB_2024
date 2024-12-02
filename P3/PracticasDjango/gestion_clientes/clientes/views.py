from django.shortcuts import render, get_object_or_404, redirect
from .models import Direccion, Cliente
from .forms import DireccionForm, ClienteForm
from django.shortcuts import redirect

from django.shortcuts import redirect

def custom_404_view(request, exception):
    return redirect('/clientes/')

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista_clientes.html', {'clientes': clientes})

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, 'clientes/agregar_cliente.html', {'form': form})

def agregar_direccion(request, cliente_id):
    cliente = Cliente.objects.get(id=cliente_id)
    if request.method == 'POST':
        form = DireccionForm(request.POST)
        if form.is_valid():
            direccion = form.save(commit=False)
            direccion.cliente = cliente
            direccion.save()
            return redirect('ver_direcciones', cliente_id=cliente.id)
    else:
        form = DireccionForm(initial={'cliente': cliente})
    return render(request, 'clientes/agregar_direccion.html', {'form': form, 'cliente': cliente})

def editar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/editar_cliente.html', {'form': form, 'cliente': cliente})

def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'clientes/eliminar_cliente.html', {'cliente': cliente})

def ver_direcciones(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    direcciones = cliente.direcciones.all()  # Obtiene todas las direcciones del cliente
    return render(request, 'clientes/ver_direcciones.html', {'cliente': cliente, 'direcciones': direcciones})

def editar_direccion(request, cliente_id, direccion_id):
    direccion = get_object_or_404(Direccion, id=direccion_id)
    if request.method == 'POST':
        form = DireccionForm(request.POST, instance=direccion)
        if form.is_valid():
            form.save()
            return redirect('ver_direcciones', cliente_id=cliente_id)  # Redirige a la vista de direcciones del cliente
    else:
        form = DireccionForm(instance=direccion)
    return render(request, 'clientes/editar_direccion.html', {'form': form, 'direccion': direccion})

def eliminar_direccion(request, cliente_id, direccion_id):
    direccion = get_object_or_404(Direccion, id=direccion_id)
    if request.method == 'POST':
        cliente_id = direccion.cliente.id  # Guarda el ID del cliente para redirigir después
        direccion.delete()
        return redirect('ver_direcciones', cliente_id=cliente_id)  # Redirige a la vista de direcciones del cliente
    return render(request, 'clientes/eliminar_direccion.html', {'direccion': direccion})