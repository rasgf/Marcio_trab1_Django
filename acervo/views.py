from django.db.models import Q
from django.shortcuts import redirect, render

from .forms import LivroForm
from .models import Livro


def lista_livros(request):
    nome = request.GET.get('q', '').strip()
    tipo = request.GET.get('tipo', '')
    categoria = request.GET.get('categoria', '')

    # Todos os critérios preenchidos entram na MESMA consulta, combinados
    # com Q() — em vez de encadear .filter() várias vezes — para não
    # disparar uma query por filtro quando o usuário combina busca + tipo
    # + categoria ao mesmo tempo.
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
