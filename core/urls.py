from django.urls import path
from . import views as views_core

urlpatterns = [
    path('' , views_core.index , name='index'),
]
