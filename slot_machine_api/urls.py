from django.urls import path
from . import views

urlpatterns = [
    path('get-reels-slot', views.get_reels_slot, name='get_reels_slot'),
]
