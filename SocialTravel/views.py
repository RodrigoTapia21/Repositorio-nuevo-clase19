from django.shortcuts import render
from SocialTravel.models import Post
def index(request):
    return render(request, "SocialTravel/index.html")

def mostrar_otro_template(request):
    
    Posts = Post.objects.all()
    
    
    
    return render(request, "SocialTravel/otra_template.html", {"posts": Posts})