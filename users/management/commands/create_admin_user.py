from typing import Any, Optional
from users.models import User
from django.core.management.base import (
    BaseCommand,
    CommandParser,
    CommandError
)
from django.db.utils import IntegrityError


class Command(BaseCommand):
    help = 'This command creates a new admin user'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            '-u',
            '--username',
            type=str,
            help='Defines a username to the admin user to be created'
        )
        parser.add_argument(
            '-p',
            '--password',
            type=str,
            help='Defines a password to the admin user to be created'
        )
        parser.add_argument(
            '-e',
            '--email',
            type=str,
            help='Defines a email to the admin user to be created'
        )

    def handle(self, *args: Any, **kwargs: Any) -> str | None:
        username = 'admin' if not kwargs['username'] else kwargs['username']
        password = (
            'admin1234' if not kwargs['password']
            else kwargs['password']
        )
        email = (
            f'{username}@mail.com' if not kwargs['email']
            else kwargs['email']
        )

        try:
            User.objects.create_superuser(
                username=username,
                password=password,
                email=email
            )
        except IntegrityError as err:
            if 'email' in err.args[0]:
                raise CommandError(f'Email `{email}` already taken')
            if 'username' in err.args[0]:
                raise CommandError(f'Username `{username}` already taken')
            else:
                raise IntegrityError

        self.stdout.write(self.style.SUCCESS(
            f'Admin `{username}` successfully created!'
        ))
