from django.shortcuts import render
from django.http import HttpResponse

from .models import Customer, Occupation, Loan

# Create your views here.

def index(request):
    return render(request, 'polls/index.html')

def customers(request):
    customer_data = Customer.objects.order_by('-date_added')
    context = {
        'customer_data': customer_data
    }
    return render(request, 'polls/customers.html', context)


'''
def customer(request, customer_id):

    customer_info = Customer.objects.get(id=customer_id)
    loan_info = customer_info.loan__set.order_by('-date_added')
    context = {
        'customer_info': customer_info,
        'loan_info': loan_info
    }

    return render(request, 'polls/customer.html', context)
'''
