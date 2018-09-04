import datetime

from menus.models import Menu
from menus import menus, menu_factory

from weather.models import HourForecast
from weather import forecast
#TODO: change update_menus so it reflects the updated model
class UpdateModels():

    DINING_COMMONS = ["Carrillo", "De La Guerra", "Ortega", "Portola"]
    menu_factory = menus.MenuFactory()
    menu_parser = menus.MenuParser()
    meal_parser = menus.MealParser()

    def update_menus(self):
        menus_list = []
        current_day_of_week = datetime.date.weekday(datetime.date.today())

        for dining_common in DINING_COMMONS:
            menus_list.append((dining_common, menu_parser.get_menu(dining_common)))

        for dc_menu in menus_list:
            dinner = meal_parser.get_dinner_menu(dc_menu[1])
            bright_meal = meal_parser.get_bright_meal(dc_menu[1])
            headings = menu_parser.get_menu_headings(dc_menu[1])
            if (len(dc_menu[1]) == 0):
                dining_common_menu = menu_factory.make_closed_menu(dc_menu[0])
            else if (current_day_of_week <= 4):
                breakfast = meal_parser.get_breakfast_menu(dc_menu[1])
                lunch = meal_parser.get_lunch_menu(dc_menu[1])
                late_night = meal_parser.get_late_night_menu(dc_menu[1])
                dining_common_menu = menu_factory.make_weekday_menu(dc_menu[0], breakfast, lunch,
                                                                    dinner, late_night, bright_meal,
                                                                    headings)
            else:
                brunch = meal_parser.get_brunch_menu(dc_menu[1])
                dining_common_menu = menu_factory.make_weekend_menu(dc_menu[0], brunch, dinner,
                                                                    bright_meal, headings)
            dining_common_menu.save()

    def update_weather(self):
        hourly_forecast = forecast.get_hourly_forecast("CA", "Goleta")
        for hour_forecast in hourly_forecast:
            forecast_time = datetime.now()
            forecast_hour = hour_forecast['FCTTIME']['hour']
            forecast_temp = hour_forecast['temp']['english']
            forecast_cond = hour_forecast['condition']
            forecast_time = forecast_time.replace(hour=forecast_hour, minute=0, second=0, microsecond=0)
            hour_forecast = HourForecast(hour=forecast_time, temperature=forecast_temp, condition=forecast_cond)
            hour_forecast.save()
