from django.core.management.base import BaseCommand

from menus.models import Menu
from menus import menus

class Command(BaseCommand):

    help = 'Create the menu db'

    def create_menu_db(self):
        DINING_COMMONS = ["Carillo", "De La Guerra", "Ortega", "Portola"]
        for dining_common_ in DINING_COMMONS:
            dining_common_menu = Menu(dining_common=dining_common_, menu=menus.get_menu(dining_common_))
            dining_common_menu.save()

    def handle(self, *args, **options):
        self.create_menu_db()
