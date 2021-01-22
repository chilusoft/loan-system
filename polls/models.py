from django.db import models

# Create your models here.

class CustomerInformation(models.Model):
    '''
        this contains all the personal information of the customers who register for a Loan
    '''

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    user_name = models.CharField(max_length=255)
    user_id_num = models.IntegerField()
    DOB = models.DateField('Date of birth')
    date_added = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=10)

    def __str__(self):

        return self.first_name + ' ' + self.last_name + ' - ' + str(self.user_id_num)

class OccupationDetails(models.Model):
    '''
        this contains the details of the applicant's place of work and occupation
    '''

    customer = models.ForeignKey(CustomerInformation, on_delete=models.CASCADE)
    current_employer = models.CharField(max_length=255)
    employer_address = models.TextField()
    job_title = models.CharField(max_length=255)
    employee_num = models.CharField(max_length=32)
    date_of_eng = models.DateTimeField('Date of Engagement')

    def __str__(self):

        return self.customer.first_name + ' ' + self.customer.last_name + ' | ' + self.job_title + ' | ' +self.current_employer


class LoanDetails(models.Model):
    '''
        contains the details of the Loan being applied for
    '''
    r15 = 0.15
    r25 = 0.25
    r35 = 0.35

    I_RATE = [
        (r15, "15%"),
        (r25, "25%"),
        (r35, "35%"),
    ]


    customer = models.ForeignKey(CustomerInformation, on_delete=models.CASCADE, primary_key=True)
    occupation = models.ForeignKey(OccupationDetails, on_delete=models.CASCADE)
    principal = models.FloatField(default=0)
    interest_rate = models.FloatField(choices=I_RATE, default=r25)
    date_of_request = models.DateTimeField(auto_now_add=True) 

    def __str__(self):

        return str(self.customer.user_id_num) + ' - ' + str(self.principal) + ' => ' + str(self.principal * (self.interest_rate + 1)) 

