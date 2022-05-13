from pyexpat import model
from re import template
from django.views.generic import (
    ListView,
    TemplateView,
	CreateView,
	UpdateView,
	DeleteView,
    DetailView
) 
from Post.models import Post

class Index(ListView):
    model = Post
    paginate_by = 2
    queryset = Post.objects.order_by('-fecha_publicacion')
    context_object_name = 'post_list'
    template_name = "index.html"

class About(TemplateView):
     template_name = "about.html"

class ListarArticle(ListView):
    model=Post
    paginate_by = 5
    queryset = Post.objects.order_by('-fecha_publicacion')
    context_object_name = 'post_list'
    template_name = "index.html"

class DetalleArticle(DetailView):
    model=Post
    context_object_name = 'detail_post'
    template_name = "article.html"

class CreateArticle(CreateView):
    model=Post
    success_url = '/'
    fields = ['titulo', 'descripcion', 'autor', 'categoria', 'contenido', 'imagen_referencial', 'publicado', 'fecha_publicacion']
    template_name = "crear.html"

class UpdateArticle(UpdateView):
    model=Post
    success_url = '/'
    fields = '__all__'
    template_name = "update.html"

class DeleteArticle(DeleteView):
    model=Post
    template_name = "borrar.html"
    success_url = '/'
