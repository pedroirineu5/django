from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import ListCarsView, CreateNewCarView, CarDetailView
from accounts.views import register_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('cars/', CarView.as_view() , name='cars_list'),
    path('new_car/', CreateNewCarView.as_view() , name='new_car'),
    path('car/<id:pk>/', CarDetailView.as_view(), name= 'car_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# import para terminar a configuração de fotos. Obs precisa do uso da lib Pillow