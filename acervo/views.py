from django.db.models import Q
from django.shortcuts import redirect, render

from .forms import LivroForm
from .models import Livro


def lista_livros(request):
    nome = request.GET.get('q', '').strip()
    tipo = request.GET.get('tipo', '')
    categoria = request.GET.get('categoria', '')

    # Q() é necessário aqui porque a busca por texto exige OR (título OU
    # autor) — filter(campo=valor) encadeado só expressa AND. Combinar
    # tudo num único Q() não muda o número de consultas ao banco (o
    # QuerySet é "lazy": só executa quando o resultado é usado), é só a
    # forma de escrever OR e AND na mesma condição, como pede o enunciado.
    filtro = Q()
    if nome:
        filtro &= Q(titulo__icontains=nome) | Q(autor__icontains=nome)
    if tipo:
        filtro &= Q(tipo_acervo=tipo)
    if categoria:
        filtro &= Q(categoria=categoria)

    livros = Livro.objects.filter(filtro)

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
