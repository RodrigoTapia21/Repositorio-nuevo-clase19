"""project URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from SocialTravel.views import (index, PostList, PostDetail, PostUpdate, PostDelete, PostCreate,
                                PostSearch, Login, Singup, Logout, PostMineList)
from django.conf import settings 
from django.conf.urls.static import static 
urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path("post/list", PostList.as_view(), name= "post-list" ),
    path("Post/Detail/<pk>", PostDetail.as_view(), name = "post-detail"),
    path("Post/update/<pk>", PostUpdate.as_view(), name = "post-update"),
    path("Post/delete/<pk>", PostDelete.as_view(), name = "post-delete"),
    path("Post/create", PostCreate.as_view(), name = "post-create"),
    path("Post/search", PostSearch.as_view(), name = "post-search"),
    path("login/", Login.as_view(), name = "login"),
    path("singup/", Singup.as_view(), name = "singup"),
    path("logout/", Logout.as_view(), name = "logout"),
    path("post/list/mine/", PostMineList.as_view(), name = "post-mine"),
]  

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)