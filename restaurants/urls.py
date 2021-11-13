from django.urls import path 
from . import views
app_name = 'restaurants'

urlpatterns = [
    path('', views.RestaurantList.as_view(), name='restaurant-list'),
    path('create', views.AddRestaurant.as_view(), name='add-restaurant'),
    path('edit/<int:pk>', views.EditRestaurant.as_view(), name='edit-restaurant'),
    path('remove/<int:pk>', views.DeleteRestaurant.as_view(), name='delete-restaurant'),
    path('detail/<int:pk>', views.RestaurantDetail.as_view(), name='restaurant-detail')
]
