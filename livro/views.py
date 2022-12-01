from django.shortcuts import redirect, render


from usuario.models import Usuario
from .models import Livro
# Create your views here.

def home(request):
    if request.session.get('usuario'):
        usuario = Usuario.objects.get(id = request.session['usuario'])
        livros = Livro.objects.filter(usuario = usuario)
        return render(request, 'home.html', {'livros':livros})
    else:
        return redirect('/auth/login/?status=2')
