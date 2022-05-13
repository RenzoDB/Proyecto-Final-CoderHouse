from django.urls import path
from .views import *

urlpatterns = [
    path('', Index.as_view(), name = 'index'),
    path('about', About.as_view(), name = 'about'),
    path('articulos', ListarArticle.as_view(), name = 'article'),
    path('detalle/<slug:slug>', DetalleArticle.as_view(), name = 'detalle'),   
    path('crear', CreateArticle.as_view(), name = 'crear'),
    path('borrar/<slug:slug>', DeleteArticle.as_view(), name = 'borrar'),
    path('update/<pk>', UpdateArticle.as_view(), name = 'update'),
    ]