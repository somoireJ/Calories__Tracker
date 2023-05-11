from django.db import models

class Food(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()

    def __str__(self):
        return self.name

class Day(models.Model):
    date = models.DateField(auto_now_add=True)
    foods = models.ManyToManyField(Food)

    def __str__(self):
        return str(self.date)
