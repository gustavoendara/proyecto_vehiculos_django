from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView
from django.conf.urls import handler403
from vehiculo.views import permission_denied_view

urlpatterns = [
    path('', views.index, name='index'),
    path('vehiculo/add/', views.add_vehiculo, name='add_vehiculo'),
    path('vehiculo/listar/', views.listar_vehiculos, name='listar_vehiculos'),
    path('vehiculo/register/', views.register, name='register'),
    path('vehiculo/login/', views.login_view, name= 'login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]

handler403 = permission_denied_view