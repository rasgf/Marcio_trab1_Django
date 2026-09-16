# Biblioteca — Trabalho Django (Aulas 4 e 5)

Projeto Django que consolida as atividades práticas da **Aula 4** (models,
migrações, ORM e Admin) e da **Aula 5** (views, URLs, templates e forms),
com os requisitos adicionais do trabalho: tipo de acervo, categoria e
pesquisa.

## Requisitos do trabalho

Ver [`docs/enunciado.txt`](docs/enunciado.txt). Resumo do que foi
implementado:

- [x] Model `Livro` com **tipo de acervo** (Digital ou Físico)
- [x] Model `Livro` com **categoria** (classes 000 a 900, conforme a
      Classificação Decimal indicada no enunciado)
- [x] Pesquisa por **nome** (título/autor), **tipo** e **categoria** na
      página `/livros/`
- [x] Histórico do repositório com o passo a passo das aulas 4 e 5, em
      commits separados

## Estrutura

- **Projeto**: `biblioteca/`
- **App**: `acervo/`
  - `models.py` — model `Livro`
  - `admin.py` — cadastro no Django Admin
  - `forms.py` — `LivroForm` (ModelForm)
  - `views.py` — `lista_livros` (listagem + busca) e `novo_livro`
    (cadastro)
  - `urls.py` — rotas do app
  - `templates/acervo/` — `base.html`, `lista.html`, `form.html`
  - `static/acervo/estilo.css`
  - `fixtures/livros.json` — 10 livros de exemplo

## Como rodar

```bash
# 1. ambiente virtual
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 2. dependências
pip install -r requirements.txt

# 3. variáveis de ambiente
cp .env.example .env
# edite o .env se quiser usar PostgreSQL (ver comentários no arquivo);
# por padrão o projeto já roda com SQLite, sem configuração extra.

# 4. banco de dados
python manage.py migrate

# 5. (opcional) carregar livros de exemplo
python manage.py loaddata livros

# 6. usuário administrador
python manage.py createsuperuser

# 7. rodar
python manage.py runserver
```

Acesse:

- `http://127.0.0.1:8000/livros/` — lista e busca de livros
- `http://127.0.0.1:8000/livros/novo/` — cadastrar um livro
- `http://127.0.0.1:8000/admin/` — Django Admin

## Pesquisa

A página de listagem aceita os parâmetros de busca (combináveis) via
query string:

- `?q=` — busca por título ou autor
- `?tipo=digital` ou `?tipo=fisico`
- `?categoria=000` até `?categoria=900`

Exemplo: `/livros/?q=machado&categoria=800`

## Aulas de referência

- **Aula 4 — Django na Prática I**: venv, projeto, app, model, migrações,
  ORM, Django Admin, PostgreSQL e `python-dotenv`.
- **Aula 5 — Django na Prática II**: views, URLs, templates, herança de
  templates, arquivos estáticos e forms (`ModelForm`).
