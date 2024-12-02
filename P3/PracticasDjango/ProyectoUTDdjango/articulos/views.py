from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Article, Category

@login_required(login_url='inicio')
def list_art(request):
    articulos = Article.objects.all()  # Obtén todos los artículos
    return render(request, 'articulos/listado_art.html', {
        'title': 'Articulos',
        'content': 'Varios Articulos',
        'articulos': articulos
    })

@login_required(login_url='inicio')
def list_cat(request):
    categorias = Category.objects.all()
    return render(request, 'categorias/listado_cat.html', {
        'title': 'Categorias',
        'content': 'Varios Articulos',  # Aquí se agregó la coma
        'categorias': categorias
    })