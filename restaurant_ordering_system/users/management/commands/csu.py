from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """
    Класс - команда для создания суперпользователя
    """

    def handle(self, *args, **options):
        user = User.objects.create(
            email='alex77bel@yandex.ru',
            first_name='aleksandr',
            last_name='churilin',
            is_staff=True,
            is_superuser=True,
            is_active=True,
            position='Admin'
        )

        user.set_password('123')

        user.save()
