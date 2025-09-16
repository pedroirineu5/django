from django.urls import path

from . import views


#homeApp/
urlpatterns = [
    path('', views.home),
    path('exemplo1/', views.home2)
]

