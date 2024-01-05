from django.urls import path
from . import views
urlpatterns = [
    path('add_car',views.AddCarView.as_view(),name='add_car')
]
