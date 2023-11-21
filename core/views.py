from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required

def index(request):
    contexto = {'titulo' : 'Registro | Login'}
    if request.method == 'GET':
        return render(request, 'core/index.html' , contexto)


def login(request):
    contexto = {'titulo' : 'Logeando'}
    if request.method == 'GET':
        return redirect('/')
    if request.method == 'POST':
        correo = request.POST['log_in_usuario']
        clave = request.POST['pass_usuario']
        print(correo  , clave)
        return redirect('/success/')

def success(request):
    # valor = request.POST['jugador']
    # print(valor)
    return redirect('/perfil_jugador/')


def perfil_jugador(request):
    contexto = {'titulo' : 'Perfil Jugador'}
    return render(request , 'core/perfil_jugador.html' , contexto)

def perfil_centro(request):
    contexto = {'titulo' : 'Perfil Centro'}
    return render(request , 'core/perfil_centro.html' , contexto)

def muro_principal(request):
    return render(request , 'core/muro_principal.html')