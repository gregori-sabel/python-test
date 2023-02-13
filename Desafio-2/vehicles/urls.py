from django.urls import path
from . import views

# TODO as URL tem que ser /api/v1/customer_add

app_name = 'vehicles'
urlpatterns = [
    path('', views.index, name='index'),
    
    path('list_customer', views.listCustomer, name='listCustomer'),
    path('list_customer/<int:user_id>', views.listCustomerById, name='listCustomerById'),
        
    path('list_vehicle', views.listVehicle, name='listVehicle'),
    path('list_vehicle/<int:vehicle_id>', views.listVehicleById, name='listVehicleById'),
    path('search_vehicle', views.searchVehicle, name='searchVehicle'),
    
    path('customer_form', views.customerForm, name='customerForm'),
    path('api/v1/customer_add', views.customerAdd, name='customerAdd'),
    
    path('vehicle_form', views.vehicleForm, name='vehicleForm'),
    path('api/v1/vehicle_add', views.vehicleAdd, name='vehicleAdd'),
    # path('', views.IndexView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultView.as_view(), name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]