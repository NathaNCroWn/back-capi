from django.contrib import admin
from django.urls import path, include
from . import views
#
urlpatterns = [
    path('create-producto', views.crear_producto),
    path('actualizar-producto/<int:id>', views.actualizar_producto),
    path('',views.ver_producto), 
    path('borrar-producto/<int:id>', views.eliminar_producto )
]