from django.contrib import admin

from .models import Customer, Loan, Occupation

# Register your models here.

admin.site.register(Customer)
admin.site.register(Loan)
admin.site.register(Occupation)
