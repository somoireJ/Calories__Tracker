# from django.urls import path
# from . import views

# # app_name = 'myApp'

# urlpatterns = [
#     path('', views.home, name='home'),
#     path('add_food/', views.add_food, name='add_food'),
#     path('food/', views.food, name='food'),
#     #    path('food/<int:pk>/', views.food, name='food'),
#     # path('food/<int:pk>/edit/', views.edit_food, name='edit_food'),
#     # path('food/<int:pk>/delete/', views.delete_food, name='delete_food'),
#     path('edit_food/', views.edit_food, name='edit_food'),
#     path('delete_food/', views.delete_food, name='delete_food'),

from django.urls import path
from . import views

app_name = 'myApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_food/', views.add_food, name='add_food'),
    path('food/', views.food, name='food'),
    path('food/<int:pk>/', views.food, name='food_detail'),
    path('food/<int:pk>/edit/', views.edit_food, name='edit_food'),
    path('delete_food/<int:pk>/', views.delete_food, name='delete_food'),
]

