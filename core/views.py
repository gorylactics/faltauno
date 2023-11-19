from django.shortcuts import render , redirect

def index(request):
    contexto = {'titulo' : 'Registro | Login'}
    if request.method == 'GET':
        return render(request, 'core/index.html' , contexto)
