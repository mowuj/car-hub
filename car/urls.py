from django.urls import path
from . import views
urlpatterns = [
    path('add_car',views.AddCarView.as_view(),name='add_car'),
    path('car_detail<int:id>', views.CarDetailView.as_view(), name='car_detail'),
]
