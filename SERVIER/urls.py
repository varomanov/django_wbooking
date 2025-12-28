from django.contrib import admin
from django.urls import path
from WorkplaceBooking import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.booking, name='booking'),
    path('/journal', views.journal, name='journal'),
    path('/floor', views.floor, name='floor'),
    path('/kir', views.kir, name='kir'),
]
