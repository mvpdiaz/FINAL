"""
URL configuration for ap40proyecto_001 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views
from app_ListaDeTareas.views import PrincipalView
from app_ListaDeTareas.views import ProfileView
from app_ListaDeTareas.views import redireccionar_a_lista_de_tareas
from rest_framework.routers import DefaultRouter
from app_ListaDeTareas.views import TareaViewSet
from app_ListaDeTareas.views import TareaListCreateView, TareaDetailView

#from django.conf.urls import url

from rest_framework.authtoken.views import obtain_auth_token
from app_ListaDeTareas import views

router = DefaultRouter()
router.register(r'tareas', TareaViewSet)

urlpatterns =[
    path('users/', include('users.urls')),
    path("login/", auth_views.LoginView.as_view(), name ="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('admin/', admin.site.urls),
    path(r'^auth/',obtain_auth_token),
    path('', PrincipalView.as_view(), name='inicio'),
    path('accounts/profile/', ProfileView.as_view(), name='profile'),
    path('accounts/profile/redirect/', redireccionar_a_lista_de_tareas, name='redirect_to_tareas'),
    path('api/tareas/', TareaListCreateView.as_view(), name='tarea-list-create'),
    path('api/tareas/<int:pk>/', TareaDetailView.as_view(), name='tarea-detail'),
    
]
urlpatterns += router.urls
