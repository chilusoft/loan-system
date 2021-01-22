from django.shortcuts import render
from django.http import HttpResponse

from .models import CustomerInformation

# Create your views here.

def index(request):
    return render(request, 'polls/index.html')

def customers(request):
    customer_data = CustomerInformation.objects.order_by('-date_added')
    context = {
        'customer_data': customer_data
    }
    return render(request, 'polls/customers.html', context)