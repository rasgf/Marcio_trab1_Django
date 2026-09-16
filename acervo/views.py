from django.db.models import Q
from django.shortcuts import redirect, render

from .forms import LivroForm
from .models import Livro


def lista_livros(request):
    livros = Livro.objects.all()

    nome = request.GET.get('q', '').strip()
    tipo = request.GET.get('tipo', '')
    categoria = request.GET.get('categoria', '')

    if nome:
        livros = livros.filter(Q(titulo__icontains=nome) | Q(autor__icontains=nome))
    if tipo:
        livros = livros.filter(tipo_acervo=tipo)
    if categoria:
        livros = livros.filter(categoria=categoria)

    contexto = {
        'livros': livros,
        'tipos': Livro.TipoAcervo.choices,
        'categorias': Livro.Categoria.choices,
        'filtro_q': nome,
        'filtro_tipo': tipo,
        'filtro_categoria': categoria,
    }
    return render(request, 'acervo/lista.html', contexto)


def novo_livro(request):
    if request.method == 'POST':
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = LivroForm()
    return render(request, 'acervo/form.html', {'form': form})
