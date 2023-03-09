from django import forms 
from SocialTravel.models import Post 

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"#vamos a usar todos los campos de la clase Post en models.py 
        