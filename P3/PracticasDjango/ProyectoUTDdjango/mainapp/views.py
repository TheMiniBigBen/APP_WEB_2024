from django.shortcuts import render

def index(request):
    return render(request, 'mainapp/index.html')
        
def about(requets):
    return render(requets, 'mainapp/about.html',{
        'title':'Acerca de',
        'content':'..:: Somos un equipo de Desarrollo de SW con Django ::..'
    })
    
def mision(requets):
    return render(requets, 'mainapp/mision.html',{
        'title':'mision',
        'content':'..:: Somos un equipo de Desarrollo de SW con Django ::..'
    })
    
def vision(requets):
    return render(requets, 'mainapp/vision.html',{
        'title':'vision',
        'content':'..:: Somos un equipo de Desarrollo de SW con Django ::..'
    })


def error404(request, exception):
    return render(request, 'mainapp/404.html', status=404)
