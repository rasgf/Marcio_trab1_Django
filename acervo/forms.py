from django import forms
from django.utils import timezone

from .models import Livro


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autor', 'ano', 'tipo_acervo', 'categoria', 'disponivel']

    def clean_ano(self):
        ano = self.cleaned_data.get('ano')
        ano_atual = timezone.now().year
        if ano and ano > ano_atual:
            raise forms.ValidationError(
                f'O ano de publicação não pode ser posterior a {ano_atual}.'
            )
        return ano
