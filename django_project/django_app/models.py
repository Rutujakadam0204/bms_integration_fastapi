from django.db import models

# Create your models here.

"""Contact model saving all Personal information about contact"""


class PersonalInfo(models.Model):
    LEAD_STATUS_CHOICES = [
        ('', 'Lead Status Choice'),
        ('New', 'New'),
        ('Open', 'Open'),
        ('In Progress', 'In Progress'),
        ('Open Deal', 'Open Deal'),
        ('Unqualified', 'Unqualified'),
    ]

    LIFE_CYCLE_STAGE_CHOICES = [
        ('', 'Life Cycle Stage'),
        ('Lead', 'Lead'),
        ('Marketing qualified lead', 'Marketing qualified lead'),
        ('Sales qualified lead', 'Sales qualified lead'),
        ('Opportunity', 'Opportunity'),
        ('Customer', 'Customer'),
        ('Evangelist', 'Evangelist'),
        ('Others', 'Others')
    ]

    PREFIX_CHOICES = [
        ('', 'Select Prefix'),
        ('Mr.', 'Mr.'),
        ('Mrs.', 'Mrs.'),
        ('Ms.', 'Ms.'),
        ('Father', 'Father'),
        ('Elder', 'Elder'),
        ('Brother', 'Brother'),
        ('Sister', 'Sister'),
        ('Rabbi', 'Rabbi'),
        ('Rev', 'Rev'),
        ('Capt.', 'Capt.'),
        ('Chief', 'Chief'),
        ('Cmdr.', 'Cmdr.'),
        ('Lt Col.', 'Lt Col.'),
        ('Lt.', 'Lt.'),
        ('Col.', 'Col.'),
        ('Gen.', 'Gen.'),
        ('Hon.', 'Hon.'),
        ('Maj.', 'Maj.'),
        ('MSgt.', 'MSgt.'),
        ('Adm.', 'Adm.'),
        ('Atty.', 'Atty.'),
        ('Dean', 'Dean'),
        ('Prof.', 'Prof.'),
        ('Dr.', 'Dr.'),
        ('Prince', 'Prince'),
    ]

    GENDER_CHOICES = [
        ('', 'Select Gender'),
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Third Gender', 'Third Gender'),
        ('Decline To Answer', 'Decline To Answer'),
    ]

    SUFFIX_CHOICES = [
        ('', 'Select Suffix'),
        ('II', 'II'),
        ('III', 'III'),
        ('IV', 'IV'),
        ('CPA', 'CPA'),
        ('DDS', 'DDS'),
        ('ESq', 'ESq'),
        ('JD', 'JD'),
        ('Sr', 'Sr'),
        ('Jr', 'Jr'),
        ('DO', 'DO'),
        ('MD', 'MD'),
        ('PhD', 'PhD'),
        ('Ret', 'Ret'),
        ('RN', 'RN'),
    ]

    lead_status = models.CharField(max_length=20, choices=LEAD_STATUS_CHOICES, default='New')
    life_cycle_stage = models.CharField(max_length=50, choices=LIFE_CYCLE_STAGE_CHOICES, default='Lead')
    prefix = models.CharField(max_length=30, choices=PREFIX_CHOICES, blank=True, default='Mr.')
    first_name = models.CharField(max_length=30, help_text='Enter first name')
    middle_name = models.CharField(max_length=30, blank=True, help_text='Enter middle name')
    last_name = models.CharField(max_length=30,blank=True, help_text='Enter last name')


    def __str__(self):
        return self.first_name + ' ' + self.last_name


class Invoice(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(blank=True, null=True)

"""Company model saving all information about company"""
class CompanyInfo(models.Model):
    name = models.CharField(max_length=100, blank=True, help_text='Enter name')
    domain_name = models.CharField(max_length=50, blank=True, help_text='Enter domain name')
    industry = models.CharField(max_length=100, blank=True, help_text='Enter indistry')
    c_country = models.CharField(max_length=50, blank=True, help_text='Enter country')
    c_state = models.CharField(max_length=50, blank=True, help_text='Enter state')
    c_city = models.CharField(max_length=50, blank=True, help_text='Enter city')

    def __str__(self):
        return self.name


"""Payment Receivable"""

class AccountsReceivable(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True)
    contact = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE, null=True)
    amount = models.BigIntegerField(null=True, default=0)
    created_at = models.DateTimeField()
    paid = models.BooleanField(default=False)

    def __str__(self):
        return str(self.invoice)

"""Payment Payable"""

class AccountsPayable(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, null=True)
    outstanding_amount = models.BigIntegerField(null=True, default=0)
    amount_paid = models.BigIntegerField(null=True, default=0)
    payment_status = models.CharField(blank=True, max_length=50, help_text='payment status')
    created_at = models.DateTimeField(blank=True)

    def __str__(self):
        return str(self.invoice)
