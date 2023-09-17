from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from rest_framework import viewsets
from .models import Tarea
from .serializers import TareaSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth import login, authenticate


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

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class TareaListCreateView(ListCreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class TareaDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
