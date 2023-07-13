from django.urls import path
from .views import clientes_list,clientes_detalle

urlpatterns = [
    path('clientes/', clientes_list, name = 'categoria_list'),
    path('clientes/<int:pk>',clientes_detalle, name = 'categoria_detalle'),
]