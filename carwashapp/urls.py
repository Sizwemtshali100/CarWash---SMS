from django.urls import path
from . import views

urlpatterns = [
    path('', views.LoginPage, name='LoginPage'),
    path('listView/', views.home, name='home'),
    #path('send_sms_view/', views.send_sms_view, name='send_sms_view'),
    path('VehicleWashDetails/<int:list_id>', views.VehicleWashDetails, name='VehicleWashDetails'),
    path('RegistrationPage/', views.RegistrationPage, name='RegistrationPage'),
    path('CarWashApplication/', views.CarWashApplication, name='CarWashApplication'),

]
