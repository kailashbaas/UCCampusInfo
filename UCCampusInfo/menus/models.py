from django.db import models


class Menu(models.Model):
    dining_common = models.CharField(max_length=12)
    breakfast_menu = models.TextField()
    brunch_menu = models.TextField()
    lunch_menu = models.TextField()
    dinner_menu = models.TextField()
    late_night_menu = models.TextField()
    bright_meal_menu = models.TextField()
    menu_headings = models.TextField()

    def __str__(self):
        return self.dining_common + " Dinner: " + self.dinner_menu
