from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import redirect
from rest_framework import viewsets
from .models import Tarea
from .serializers import TareaSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Clase para la vista del perfil de usuario
class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"  # Nombre del template del perfil

# Clase para la vista de inicio de sesión (puedes personalizarla según tus necesidades)
class CustomLoginView(LoginView):
    template_name = "login.html"  # Nombre del template de inicio de sesión
    redirect_authenticated_user = True

# Clase para la vista de cierre de sesión (puedes personalizarla según tus necesidades)
class CustomLogoutView(LogoutView):
    next_page = reverse_lazy("user_profile")  # Redirige a la página de perfil después del cierre de sesión

# Clase para la vista principal
class PrincipalView(TemplateView):
    template_name = "principal.html"

    def get(self, request):
        return render(request, self.template_name)
    
def redireccionar_a_lista_de_tareas(request):
    # Define la URL de la lista de tareas en Next.js
    url_lista_de_tareas = "http://localhost:3000/lista-tarea"  # Reemplaza con la URL correcta
    
    return redirect(url_lista_de_tareas)

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class TareaListCreateView(ListCreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class TareaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
