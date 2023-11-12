from django.core.management.base import BaseCommand

from users.models import User


class Command(BaseCommand):
    help = 'Создание суперюзера'

    def handle(self, *args, **kwargs):
        user = User.objects.create(
            email='igor.zinoviev08@yandex.ru',
            first_name='Admin',
            last_name='Skypro',
            is_staff=True,
            is_superuser=True
            is_verified_email= True

        )
        user.set_password('qwerty123')
        user.save()