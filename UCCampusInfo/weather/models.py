from django.db import models


class HourForecast(models.Model):
    """
    Weather forecast for a specific hour
    @hour the hour the weather forecast is for
    @temperature the forecasted temperature
    @condition the forecasted condition
    """
    fct_hour = models.DateTimeField('forecast time')
    temperature = models.IntegerField()
    condition = models.CharField(max_length=50)
    civil_time = models.CharField(max_length=8)

    def __str__(self):
        return self.civil_time + ": " + str(self.temperature) + "&#176;F" + " and " + self.condition
