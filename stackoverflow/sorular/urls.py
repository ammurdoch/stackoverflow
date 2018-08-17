from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ilk-soru', views.ilk, name='ilk')
]