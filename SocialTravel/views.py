from django.shortcuts import render
from SocialTravel.models import Post
from SocialTravel.forms import PostForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

def index(request):
    return render(request, "SocialTravel/index.html")


def mostrar_posts(request):
    context = {
         "posts": Post.objects.all(),
         "form": PostForm(),
         }

    
    return render(request, "SocialTravel/admin_post.html", context)


def agregar_post(request):
    post_form = PostForm(request.POST)
    post_form.save()
    context = {
         "posts": Post.objects.all(),
         "form": PostForm(),
         }

    return render(request, "SocialTravel/admin_post.html", context)


def buscar_post(request):
    criterio = request.GET.get("criterio")
    context = { "posts": Post.objects.filter(carousel_caption_title__icontains=criterio).all()}
    return render(request, "SocialTravel/admin_post.html", context)


class PostList(ListView):
    model = Post
    context_object_name = "posts" #para cambiar el nombre en post_list.html {% for post in "posts" %}
    
class PostDetail(DetailView):
    model = Post
    context_object_name = "post" 
    
class PostUpdate(UpdateView):
    model = Post
    success_url = reverse_lazy("post-list")#una vez actualizado vuelve a list
    fields = "__all__"
    
class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy("post-list")
    
class PostCreate(CreateView):
    model = Post 
    success_url = reverse_lazy("post-list")
    fields = "__all__"
    
class PostSearch(ListView):
    model = Post 
    context_object_name = "posts" 
    
    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result = Post.objects.filter(carousel_caption_title__icontains=criterio).all()
        return result
    