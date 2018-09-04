from menus.models import Menu

class MenuFactory():

    def __init__(self):
        self.menu_dict = {"Breakfast": [],
                     "Brunch": [],
                     "Lunch": [],
                     "Dinner": [],
                     "Late Night": [],
                     "Bright Meal": [],
                     "Headings": []}

    def make_closed_menu(self, dining_common):
        return self.make_menu(dining_common, menu_dict)

    def make_weekday_menu(self, dining_common, breakfast, lunch, dinner, late_night, bright_meal, headings):
        self.menu_dict['Breakfast'] = breakfast
        self.menu_dict['Lunch'] = lunch
        self.menu_dict['Dinner'] = dinner
        self.menu_dict['Late Night'] = late_night
        self.menu_dict['Bright Meal'] = bright_meal
        self.menu_dict['Headings'] = headings
        return self.make_menu(dining_common, self.menu_dict)

    def make_weekend_menu(self, brunch, dinner, bright_meal, headings):
        self.menu_dict['Brunch'] = brunch
        self.menu_dict['Dinner'] = dinner
        self.menu_dict['Bright Meal'] = bright_meal
        self.menu_dict['Headings'] = headings
        return self.make_menu(dining_common, self.menu_dict)

    def make_menu(self, dining_common, menu_dictionary):
        dining_common_menu = Menu(dining_common=dining_common,
                                  breakfast_menu = menu_dictionary['Breakfast'],
                                  brunch_menu = menu_dictionary['Brunch'],
                                  lunch_menu = menu_dictionary['Lunch'],
                                  dinner_menu = menu_dictionary['Dinner'],
                                  late_night_menu = menu_dictionary['Late Night'],
                                  bright_meal_menu = menu_dictionary['Bright Meal'],
                                  menu_headings = menu_dictionary['Headings'])
        return dining_common_menu
