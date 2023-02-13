from django.http import Http404
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import User, Vehicle
from django.shortcuts import get_object_or_404


from django.views import generic

# class IndexView(generic.ListView):
#   template_name = 'vehicles/index.html'
#   context_object_name = 'latest_question_list'

  # def get_queryset(self):
  #   """Return the last five published questions."""
  #   return Question.objects.order_by('-pub_date')[:5]

# class DetailView(generic.DetailView):
#   model = Vehicle
#   template_name = 'vehicles/detail.html'

# class ResultView(generic.DetailView):
#   model = Vehicle
#   template_name = 'vehicles/detail.html'

# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

def index(request):
  vehicles_all = Vehicle.objects.all()
  context = {'vehicles_all': vehicles_all}
  return render(request, 'vehicles/index.html', context)

# def detail(request, question_id):
#   question = get_object_or_404(Question, pk=question_id)
#   return render(request, 'vehicles/detail.html', {'question': question})

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'vehicles/results.html', {'question': question})

def listVehicle(request):
  vehicles = Vehicle.objects.all()
  context = {'vehicles': vehicles}
  return render(request, 'vehicles/listVehicle.html', context)

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
  return request.status(200)

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



# def vote(request, question_id):
#   question = get_object_or_404(Question, pk=question_id)
#   try:
#     selected_choice = question.choice_set.get(pk=request.POST['choice'])
#   except (KeyError, Choice.DoesNotExist):
#     return render(request, 'vehicles/detail.html', {
#       'question': question,
#       'error_message': "You didn't select a choice."
#     })
#   else:
#     selected_choice.votes += 1
#     selected_choice.save()
#     # Always return an HttpResponseRedirect after successfully dealing
#     # with POST data. This prevents data from being posted twice if a
#     # user hits the Back button.
#     return HttpResponseRedirect(reverse('vehicles:results', args=(question.id,)))
