from django.urls import path

from . import views

urlpatterns = [
    path('', views.start_game, name='start_game'),
    path('display', views.display, name='display'),
    path('choose_area', views.choose_area, name='choose_area')

]


