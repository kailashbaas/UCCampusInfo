from lxml import html
import requests


class MenuParser:


    def __init__(self):
        self.carrillo_xpath = "//div[@id='Carrillo-body']//div[@class='panel-heading']/h5/text()"
        #self.carrillo_xpath += " | //div[@id='Carrillo-body']//div[@class='panel-heading']/h5/small/text()"
        self.carrillo_xpath += " | //div[@id='Carrillo-body']//div[@class='panel-body']//dd/text()"
        self.carrillo_headings_xpath = "//div[@id='Carrillo-body']//div[@class='panel-body']//dt/text()"
        self.carrillo_xpath += " | " + self.carrillo_headings_xpath

        self.dlg_xpath = "//div[@id='DeLaGuerra-body']//div[@class='panel-heading']//h5/text()"
        #self.dlg_xpath += " | //div[@id='DeLaGuerra-body']//div[@class='panel-heading']/h5/small/text()"
        self.dlg_xpath += " | //div[@id='DeLaGuerra-body']//div[@class='panel-body']//dd/text()"
        self.dlg_headings_xpath = "//div[@id='DeLaGuerra-body']//div[@class='panel-body']//dt/text()"
        self.dlg_xpath += " | " + self.dlg_headings_xpath

        self.ortega_xpath = "//div[@id='Ortega-body']//div[@class='panel-heading']//h5/text()"
        #self.ortega_xpath += " | //div[@id='Ortega-body']//div[@class='panel-heading']/h5/small/text()"
        self.ortega_xpath += " | //div[@id='Ortega-body']//div[@class='panel-body']//dd/text()"
        self.ortega_headings_xpath = "//div[@id='Ortega-body']//div[@class='panel-body']//dt/text()"
        self.ortega_xpath += " | " + self.ortega_headings_xpath

        self.portola_xpath = "//div[@id='Portola-body']//div[@class='panel-heading']//h5/text()"
        #self.portola_xpath += " | //div[@id='Portola-body']//div[@class='panel-heading']/h5/small/text()"
        self.portola_xpath += " | //div[@id='Portola-body']//div[@class='panel-body']//dd/text()"
        self.portola_headings_xpath = "//div[@id='Portola-body']//div[@class='panel-body']//dt/text()"
        self.portola_xpath += " | " + self.portola_headings_xpath

        self.dining_commons_xpaths = {
                                    "Carrillo": self.carrillo_xpath,
                                    "De La Guerra": self.dlg_xpath,
                                    "Ortega": self.ortega_xpath,
                                    "Portola": self.portola_xpath
                                }

        self.menu_headings_xpaths = {
                                "Carrillo": self.carrillo_headings_xpath,
                                "De La Guerra": self.dlg_headings_xpath,
                                "Ortega": self.ortega_headings_xpath,
                                "Portola": self.portola_headings_xpath
                                }


    def get_menu(self, dining_common):
        """
        @param dining_common the dining common to get a menu from
        """
        return self.get_parsed_menu(dining_common, self.dining_commons_xpaths)



    def get_parsed_menu(self, dining_common, xpath_dict):
        try:
            page = requests.get('https://appl.housing.ucsb.edu/menu/day/')
            tree = html.fromstring(page.content)
            return self.format_parsed_menu(tree.xpath(xpath_dict[dining_common]))
        except requests.exceptions.RequestException as e:
            return ['An error occurred when getting the menus']


    def format_parsed_menu(self, parsed_menu):
        """
        Removes whitespace on left and right sides of menu items and any
        empty strings from the menu
        """
        return [item.strip() for item in parsed_menu if item != '']

    def get_menu_headings(self, dining_common):
        return self.get_parsed_menu(dining_common, self.menu_headings_xpaths)


class MealParser():
    """
    The purpose of this class is to parse each individual meal's menu from
    the list containing the menus for every meal
    """
    menu_headings = ["Breakfast", "Brunch", "Lunch", "Dinner", "Late Night", "Bright Meal"]

    def get_breakfast_menu(self, menu):
        return self.get_submenu(menu, "Breakfast")

    def get_brunch_menu(self, menu):
        return self.get_submenu(menu, "Brunch")

    def get_lunch_menu(self, menu):
        return self.get_submenu(menu, "Lunch")

    def get_dinner_menu(self, menu):
        return self.get_submenu(menu, "Dinner")

    def get_late_night_menu(self, menu):
        return self.get_submenu(menu, "Late Night")

    def get_bright_meal_menu(self, menu):
        return self.get_submenu(menu, "Bright Meal")

    def get_submenu(self, menu, meal):
        try:
            list_index = menu.index(meal) + 1
            submenu = []
            while ((menu[list_index] not in self.menu_headings) and (list_index < len(menu))):
                submenu.append(menu[list_index])
                list_index += 1
            return submenu
        except ValueError as e:
            return ''
