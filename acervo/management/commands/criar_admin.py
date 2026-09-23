import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = (
        'Cria um superusuário a partir de ADMIN_USERNAME/ADMIN_EMAIL/'
        'ADMIN_PASSWORD, se ele ainda não existir. Feito pra rodar em todo '
        'deploy (build de produção), sem quebrar quando o usuário já existe.'
    )

    def handle(self, *args, **options):
        username = os.environ.get('ADMIN_USERNAME')
        password = os.environ.get('ADMIN_PASSWORD')
        email = os.environ.get('ADMIN_EMAIL', '')

        if not username or not password:
            self.stdout.write(
                'ADMIN_USERNAME ou ADMIN_PASSWORD não definidos, pulando '
                'criação do superusuário.'
            )
            return

        User = get_user_model()
        if User.objects.filter(username=username).exists():
            self.stdout.write(f'Superusuário "{username}" já existe.')
            return

        User.objects.create_superuser(username, email, password)
        self.stdout.write(f'Superusuário "{username}" criado.')
