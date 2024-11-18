
from django.contrib import admin
from django.urls import path, re_path
from mainapp import views
from mainapp.views import index
from mainapp.views import error404
from django.conf.urls import handler404

handler404 = error404


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('acercade/', views.about, name='acercade'),
    path('mision/', views.mision, name='mision'),
    path('vision/', views.vision, name='vision'),
    path('404/', views.error404, name='404'),
    re_path(r'^.*$', index, name='redirect_to_index'),

    ]
