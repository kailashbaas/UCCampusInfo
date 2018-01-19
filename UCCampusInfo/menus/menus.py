from lxml import html
import requests


class MenuParser:


    def __init__(self):
        self.carrillo_xpath = "//div[@id='Carrillo-body']//div[@class='panel-heading']/h5/text()"
        #self.carrillo_xpath += " | //div[@id='Carrillo-body']//div[@class='panel-heading']/h5/small/text()"
        self.carrillo_xpath += " | //div[@id='Carrillo-body']//div[@class='panel-body']//dd/text()"
        self.carrillo_headings_xpath = "//div[@id='Carrillo-body']//div[@class='panel-body']//dt/text()"
        self.carrillo_xpath += " | " + self.carrillo_headings_xpath

        self.dlg_xpath = "//div[@id='DeLaGuerra-body']//div[@class='panel-body']//h5/text()"
        #self.dlg_xpath += " | //div[@id='DeLaGuerra-body']//div[@class='panel-heading']/h5/small/text()"
        self.dlg_xpath += " | //div[@id='DeLaGuerra-body']//div[@class='panel-body']//dd/text()"
        self.dlg_headings_xpath = "//div[@id='DeLaGuerra-body']//div[@class='panel-body']//dt/text()"
        self.dlg_xpath += " | " + self.dlg_headings_xpath

        self.ortega_xpath = "//div[@id='Ortega-body']//div[@class='panel-body']//h5/text()"
        #self.ortega_xpath += " | //div[@id='Ortega-body']//div[@class='panel-heading']/h5/small/text()"
        self.ortega_xpath += " | //div[@id='Ortega-body']//div[@class='panel-body']//dd/text()"
        self.ortega_headings_xpath = "//div[@id='Ortega-body']//div[@class='panel-body']//dt/text()"
        self.ortega_xpath += " | " + self.ortega_headings_xpath

        self.portola_xpath = "//div[@id='Portola-body']//div[@class='panel-body']//h5/text()"
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


    def get_menu(self, dining_common):
        """
        @param dining_common the dining common to get a menu from
        """
        return self.get_parsed_menu(dining_common)



    def get_parsed_menu(self, dining_common):
        try:
            page = requests.get('https://appl.housing.ucsb.edu/menu/day/')
            tree = html.fromstring(page.content)
            return self.format_parsed_menu(tree.xpath(self.dining_commons_xpaths[dining_common]))
        except requests.exceptions.RequestException as e:
            return ['An error occurred when getting the menus']


    def format_parsed_menu(self, parsed_menu):
        """
        Removes whitespace on left and right sides of menu items
        """
        return [item.strip() for item in parsed_menu]
