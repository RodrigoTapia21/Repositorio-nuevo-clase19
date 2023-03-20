from django.shortcuts import render
from SocialTravel.models import Post
from SocialTravel.forms import PostForm
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin #sirve para que el usuario no pueda interactuiar si no esta autenticado/registrado

def index(request):
    return render(request, "SocialTravel/index.html")



class PostList(ListView):
    model = Post
    context_object_name = "posts" #para cambiar el nombre en post_list.html {% for post in "posts" %}
    
class PostMineList(LoginRequiredMixin, PostList):
    
    def get_queryset(self):
        return Post.objects.filter(publisher=self.request.user.id).all()
    
class PostDetail(DetailView):
    model = Post
    context_object_name = "post" 
    
#class PermisosSoloDueno(UserPassesTestMixin):#este es para no escribir tanto codigo y heredar en UPDATE Y DELETE la funcion de abajo, sino escribirla en cada uno
    #def test_func(self):
        #user_id= self.request.user.id
        #post_id= self.kwargs.get("pk")
        #return Post.objects.filter(publisher= user_id, id= post_id).exists()#asi se valida si el usuario y el id coinciden 
    
class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    success_url = reverse_lazy("post-list")#una vez actualizado vuelve a list
    fields = "__all__"
    
    def test_func(self):
        user_id= self.request.user.id
        post_id= self.kwargs.get("pk")
        return Post.objects.filter(publisher= user_id, id= post_id).exists()
    
    
class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy("post-list")
    
    def test_func(self):
        user_id= self.request.user.id
        post_id= self.kwargs.get("pk")
        return Post.objects.filter(publisher= user_id, id= post_id).exists()
    
    
class PostCreate(LoginRequiredMixin, CreateView):
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
    
class Login(LoginView):
    next_page = reverse_lazy("post-list")


class Singup(CreateView):
    form_class = UserCreationForm
    template_name = "registration/singup.html"
    success_url = reverse_lazy("post-list")
    
class Logout(LogoutView):
    template_name = "registration/logout.html"