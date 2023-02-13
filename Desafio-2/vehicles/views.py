from django.http import Http404
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import User, Vehicle
from django.shortcuts import get_object_or_404


def index(request):
  vehicles_all = Vehicle.objects.all()
  context = {'vehicles_all': vehicles_all}
  return render(request, 'vehicles/index.html', context)

def searchVehicle(request):
  try:
    user = get_object_or_404(User, pk=request.POST['customer_id'])
    vehicle = user.vehicle.get.all()[:1]
  except:
    vehicle = get_object_or_404(Vehicle, plate=request.POST['plate'])

  return listVehicleById(request, vehicle.id)

def listVehicle(request):
  vehicles = Vehicle.objects.all()
  context = {'vehicles': vehicles}
  return render(request, 'vehicles/listVehicle.html', context)

def listVehicleById(request, vehicle_id):
  vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
  context = {'vehicle': vehicle}
  return render(request, 'vehicles/listVehicleById.html', context)

def listCustomer(request):
  users = User.objects.all()
  context = {'users': users}
  return render(request, 'vehicles/listCustomer.html', context)

def listCustomerById(request, user_id):
  user = get_object_or_404(User, id=user_id)
  context = {'user': user}
  return render(request, 'vehicles/listCustomerById.html', context)


def customerForm(request):
  # vehicles_all = Vehicle.objects.all()
  # context = {'vehicles_all': vehicles_all}
  return render(request, 'vehicles/customerForm.html')

def customerAdd(request):
  user = User(id=request.POST['pk'] ,name=request.POST['name'], card=request.POST['card_id'])
  user.save()
  # return render(request, 'vehicles/customerForm.html')
  # return HttpResponseRedirect(reverse('vehicles:customerForm'))
  return render(request, 'vehicles/customerForm.html')

def vehicleForm(request):
  # vehicles_all = Vehicle.objects.all()
  # context = {'vehicles_all': vehicles_all}
  return render(request, 'vehicles/vehicleForm.html')

from django.views.decorators.csrf import csrf_exempt

# @csrf_exempt
def vehicleAdd(request):
  vehicle = Vehicle(
    id=request.POST['pk'],
    plate=request.POST['plate'], 
    model=request.POST['model'], 
    description=request.POST['description'], 
    customer_id=request.POST['customer_id'], 
  )
  vehicle.save()
  # return render(request, 'vehicles/customerForm.html')
  return HttpResponseRedirect(reverse('vehicles:vehicleForm'))
  # return request.status(200)
