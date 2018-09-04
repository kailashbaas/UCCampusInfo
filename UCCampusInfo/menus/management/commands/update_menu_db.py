from django.core.management.base import BaseCommand

from menus.models import Menu
from menus import menus

class Command(BaseCommand):

    help = 'Updates the menus database'

    def update_menus(self):
        DINING_COMMONS = ["Carrillo", "De La Guerra", "Ortega", "Portola"]
        menu_parser = menus.MenuParser()
        meal_parser = menus.MealParser()
        for dining_common_ in DINING_COMMONS:
            full_menu = menu_parser.get_menu(dining_common_)
            breakfast = meal_parser.get_breakfast_menu(dining_common_)
            brunch = meal_parser.get_brunch_menu(dining_common_)
            lunch = meal_parser.get_lunch_menu(dining_common_)
            dinner = meal_parser.get_dinner_menu(dining_common_)
            late_night = meal_parser.get_late_night_menu(dining_common_)
            bright_meal = meal_parser.get_bright_meal_menu(dining_common_)
            headings = menu_parser.get_menu_headings(dining_common_)
            Menu.objects.filter(dining_common=dining_common_).update(breakfast_menu=breakfast, brunch_menu=brunch, lunch_menu=lunch, dinner_menu=dinner, late_night_menu=late_night, bright_meal_menu=bright_meal, menu_headings=headings)

    def handle(self, *args, **options):
        self.update_menus()
