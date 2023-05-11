from django.contrib import admin
from .models import Food, Day

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'calories')

@admin.register(Day)
class DayAdmin(admin.ModelAdmin):
    list_display = ('date',)

    filter_horizontal = ('foods',)
