from django.shortcuts import render

from .models import Livro


def lista_livros(request):
    livros = Livro.objects.all()
    return render(request, 'acervo/lista.html', {'livros': livros})
