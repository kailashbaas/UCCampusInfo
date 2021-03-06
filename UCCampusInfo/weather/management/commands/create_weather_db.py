import datetime
from django.core.management.base import BaseCommand

from weather.models import HourForecast
from weather import forecast

class Command(BaseCommand):

    help = 'Initializes the weather db'

    def create_weather_db(self):
        hourly_forecast = forecast.get_hourly_forecast("CA", "Goleta")
        for hour_forecast in hourly_forecast:
            forecast_time = datetime.datetime.now()
            forecast_hour = int(hour_forecast['FCTTIME']['hour'])
            forecast_civil_time = hour_forecast['FCTTIME']['civil']
            forecast_temp = hour_forecast['temp']['english']
            forecast_cond = hour_forecast['condition']
            forecast_time = forecast_time.replace(hour=forecast_hour, minute=0, second=0, microsecond=0)
            hour_forecast = HourForecast(fct_hour=forecast_time, temperature=forecast_temp, condition=forecast_cond, civil_time=forecast_civil_time)
            hour_forecast.save()

    def handle(self, *args, **options):
        self.create_weather_db()
