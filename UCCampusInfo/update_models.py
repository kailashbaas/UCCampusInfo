import datetime

from menus.models import Menu
from menus import menus

from weather.models import HourForecast
from weather import forecast
#TODO: change update_menus so it reflects the updated model
class UpdateModels():

    DINING_COMMONS = ["Carrillo", "De La Guerra", "Ortega", "Portola"]
    menu_headings = ["Breakfast", "Brunch", "Lunch", "Dinner", "Late Night", "Bright Meal"]

    def update_menus(self):
        menus_list = []

        for dining_common in DINING_COMMONS:
            menus_list.append((dining_common, menus.get_menu(dining_common)))

        for dc_menu in menus_list:
            dining_common_menu = Menu(dining_common=dc_menu[0], menu=dc_menu[1])
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
