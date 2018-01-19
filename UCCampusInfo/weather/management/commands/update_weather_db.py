import datetime
from django.core.management.base import BaseCommand

from weather.models import HourForecast
from weather import forecast

class Command(BaseCommand):

    help = 'Updates the weather db'

    def update_weather(self):
        current_forecast = HourForecast.objects.all()
        current_hour = current_forecast[0].fct_hour.hour
        new_hourly_forecast = forecast.get_hourly_forecast("CA", "Goleta")
        for hour_forecast in new_hourly_forecast:
            forecast_time = datetime.datetime.now()
            forecast_hour = int(hour_forecast['FCTTIME']['hour'])
            forecast_civil_time = hour_forecast['FCTTIME']['civil']
            forecast_temp = hour_forecast['temp']['english']
            forecast_cond = hour_forecast['condition']
            forecast_time = forecast_time.replace(hour=forecast_hour, minute=0, second=0, microsecond=0)
            HourForecast.objects.filter(fct_hour__hour=current_hour).update(fct_hour=forecast_time, temperature=forecast_temp, condition=forecast_cond, civil_time=forecast_civil_time)
            current_hour = (current_hour + 1) % 24

    def handle(self, *args, **options):
        self.update_weather()
