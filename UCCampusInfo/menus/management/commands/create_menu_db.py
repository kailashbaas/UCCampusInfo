from django.core.management.base import BaseCommand
import datetime

from menus.models import Menu
from menus import menus, menu_factory

class Command(BaseCommand):

    help = 'Create the menu db'

    def create_menu_db(self):
        DINING_COMMONS = ["Carrillo", "De La Guerra", "Ortega", "Portola"]
        menu_parser = menus.MenuParser()
        meal_parser = menus.MealParser()
        menu_factory_ = menu_factory.MenuFactory()
        current_day_of_week = datetime.date.weekday(datetime.date.today())
        for dining_common in DINING_COMMONS:
            full_menu = menu_parser.get_menu(dining_common)
            dinner = meal_parser.get_dinner_menu(dining_common)
            bright_meal = meal_parser.get_bright_meal_menu(dining_common)
            headings = menu_parser.get_menu_headings(dining_common)
            if (len(full_menu) == 0):
                dining_common_menu = menu_factory.make_closed_menu(dining_common)
            elif (current_day_of_week <= 4):
                breakfast = meal_parser.get_breakfast_menu(dining_common)
                lunch = meal_parser.get_lunch_menu(dining_common)
                late_night = meal_parser.get_late_night_menu(dining_common)
                dining_common_menu = menu_factory_.make_weekday_menu(dining_common, breakfast, lunch,
                        dinner, late_night, bright_meal, headings)
            else:
                brunch = meal_parser.get_brunch_menu(dining_common)
                dining_common_menu = menu_factory.make_weekend_menu(dining_common, brunch, dinner, bright_meal, headings)
            dining_common_menu.save()

    def handle(self, *args, **options):
        self.create_menu_db()
