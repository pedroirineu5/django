from django.urls import path

from . import views


#homeApp/
urlpatterns = [
    path('', views.home, name='home'),
    path('exemplo1/', views.home2, name='exemplo1')
]
