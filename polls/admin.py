from django.contrib import admin

from .models import CustomerInformation, LoanDetails, OccupationDetails

# Register your models here.

admin.site.register(CustomerInformation)
admin.site.register(LoanDetails)
admin.site.register(OccupationDetails)
