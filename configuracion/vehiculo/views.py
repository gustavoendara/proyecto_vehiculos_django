from django.shortcuts import render, redirect
from .forms import VehiculoForm, CustomUserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required, login_required
from .models import Vehiculo
from django.contrib.auth.models import Permission

def index(request):
    return render(request, 'vehiculo/index.html')

def listar_vehiculo(request):
    return render(request, 'vehiculo/listar_vehiculo.html')

def add_vehiculo(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST)
        if form.is_valid():
            form.save() 
            return redirect('index') 
    else:
        form = VehiculoForm()
    
    return render(request, 'vehiculo/add_vehiculo.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user= form.save()
            
            permiso = Permission.objects.get(codename='view_listar')
            user.user_permissions.add(permiso)
            login(request, user)
            return redirect ('index')
    else:
        form =CustomUserCreationForm()
        
    return render(request, "vehiculo/register.html", {'form' : form})
    
def login_view(request):
    if request.method == 'POST':
        username= request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
    return render(request,'vehiculo/login.html', {'error':'Credenciales invalidas'}) 

@permission_required('vehiculo.view_listar', raise_exception=True)

def listar_vehiculos(request):
    vehiculos = Vehiculo.objects.all()
    vehiculos_con_categoria = []  

    for vehiculo in vehiculos:
        
        if vehiculo.precio <= 10000:
            categoria_precio = 'bajo'
        elif 10000 < vehiculo.precio <= 30000:
            categoria_precio = 'medio'
        else:
            categoria_precio = 'alto'

        
        vehiculos_con_categoria.append({
            'vehiculo': vehiculo,
            'categoria_precio': categoria_precio
        })

    
    context = {'vehiculos': vehiculos_con_categoria}
    return render(request, 'vehiculo/listar_vehiculo.html', context)



def permission_denied_view(request, exception):
    return render(request, 'vehiculo/403.html', status=403)
