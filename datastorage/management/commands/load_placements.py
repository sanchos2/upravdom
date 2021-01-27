import csv
from typing import Any

from django.core.management.base import BaseCommand, CommandError

from datastorage.models import Entrance, Placement


def create_placement(file) -> None:  # noqa: WPS110
    """Загружает из csv файла данные по помещению."""
    with open(file, 'r', encoding='utf-8') as placements:
        fields = ['placement_type', 'entrance', 'number', 'total_space', 'living_space']
        reader = csv.DictReader(placements, fields, delimiter=';')
        for row in reader:
            Placement.objects.get_or_create(
                entrance=Entrance.objects.get(number=row['entrance']),
                number=row['number'],
                placement_type=row['placement_type'],
                total_space=row['total_space'],
                living_space=row['living_space'],
            )


class Command(BaseCommand):  # noqa: WPS: D101

    help = 'Download placements to the database.'  # noqa: WPS125

    def add_arguments(self, parser):  # noqa: D102
        parser.add_argument('file', nargs='+', type=str)

    def handle(self, *args: Any, **options: Any) -> None:  # noqa: WPS110
        """Обработчик."""
        for file in options['file']:  # noqa: WPS110
            try:
                create_placement(file)
            except KeyError:
                raise CommandError('Missing required key.')
            except ValueError:
                raise CommandError('Wrong format data.')

            self.stdout.write(
                self.style.SUCCESS('Successfully added placements.'),
            )
