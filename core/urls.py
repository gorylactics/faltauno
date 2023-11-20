from django.urls import path
from . import views as views_core

urlpatterns = [
    path('' , views_core.index , name='index'), 
    path('login/' , views_core.login , name='login'),
    path('success/' , views_core.success , name='success'),
    path('perfil_jugador/' , views_core.perfil_jugador , name='perfil_jugador'),
    path('perfil_centro/' , views_core.perfil_centro , name='perfil_centro'),
    path('muro_principal' , views_core.muro_principal , name="muro_principal")
]
