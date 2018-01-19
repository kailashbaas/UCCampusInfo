from django.core.management.base import BaseCommand

from menus.models import Menu
from menus import menus

class Command(BaseCommand):

    help = 'Updates the menus database'

    def update_menus(self):
        DINING_COMMONS = ["Carrillo", "De La Guerra", "Ortega", "Portola"]
        for dining_common_ in DINING_COMMONS:
            Menu.objects.filter(dining_common=dining_common_).update(menu=menus.get_menu(dining_common_))

    def handle(self, *args, **options):
        self.update_menus()
