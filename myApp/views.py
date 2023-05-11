from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages
from .models import Food
from .forms import FoodForm


def home(request):
    foods = Food.objects.all()
    total_calories = sum([food.calories for food in foods])
    context = {
        'foods': foods,
        'total_calories': total_calories
    }
    return render(request, 'home.html', context)



def add_food(request):
    form = FoodForm()
    if request.method == 'POST':
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food added successfully')
            return redirect('myApp:home')
    context = {'form': form}
    return render(request, 'add_food.html', context)


# def edit_food(request, pk):
#     food = get_object_or_404(Food, id=pk)
#     form = FoodForm(instance=food)
#     if request.method == 'POST':
#         form = FoodForm(request.POST, instance=food)
#         if form.is_valid():
#             form.save()
#             return redirect('food')
#     context = {'form': form}
#     return render(request, 'edit_food.html', context)



def edit_food(request, pk):
    food = get_object_or_404(Food, id=pk)
    form = FoodForm(instance=food)
    if request.method == 'POST':
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            messages.success(request, 'Food updated successfully')
            return redirect('myApp:food')
    context = {'form': form}
    return render(request, 'edit_food.html', context)



def delete_food(request, pk):
    food = get_object_or_404(Food, id=pk)
    if request.method == 'POST':
        food.delete()
        messages.success(request, 'Food deleted successfully')
        return redirect('myApp:food')
    context = {'food': food}
    return render(request, 'delete_food.html', context)


def food(request):
    foods = Food.objects.all()
    context = {'foods': foods}
    return render(request, 'food.html', context)
