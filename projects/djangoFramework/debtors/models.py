from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
#import datetime
from django.core.urlresolvers import reverse
# Create your models here.

class Company(models.Model):
    user = models.ForeignKey(User)
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=200)
    company_city = models.CharField(max_length=50)
    company_state = models.CharField(max_length=2)
    company_zip = models.CharField(max_length=15)
    company_contact_person = models.CharField(max_length=100)
    company_phone = models.CharField(max_length=25)
    def __str__(self):
        return self.company_name


class Debtor(models.Model):
    debtor_name = models.CharField(max_length=100, unique=True)
    debtor_added_by = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    def __str__(self):
        return self.debtor_name
    def get_absolute_url(self):
        return "/debtors/%i/" % self.id

class Debt(models.Model):
    debtor_name = models.ForeignKey(Debtor, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=2, null=True)
    zip = models.CharField(max_length=15, null=True)
    phone = models.CharField(max_length=25, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    debt_date = models.DateField('date of debt')
    debt_amount = models.IntegerField(default=0)
    def __str__ (self):
        return self.debtor.debtor_name

class Comment(models.Model):
    user = models.ForeignKey(User)
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=255)
    comment_date = models.DateTimeField('date of comment')
    def __str__(self):
        return self.debtor.debtor_name

class Crime(models.Model):
    causeNumber = models.CharField(max_length = 15)
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE)
    address = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=50, null=True)
    state = models.CharField(max_length=2, null=True)
    zip = models.CharField(max_length=15, null=True)
    sex = models.CharField(max_length=1, null=True)
    race = models.CharField(max_length=3, null=True)
    dob = models.DateField('date of birth', null=True, blank=True)
    offense_date = models.DateTimeField('date of offense',  null=True, blank=True)
    offense_text = models.CharField(max_length=100, null=True, blank=True)
    offense_type = models.CharField(max_length=10,  null=True, blank=True)
    case_text = models.CharField(max_length=20,  null=True, blank=True)
    disposition_text = models.CharField(max_length=40, null=True, blank=True)
    judgement_date = models.DateTimeField('date of judgement',  null=True, blank=True)
    judgement_text = models.CharField(max_length=40,  null=True, blank=True)
    sentence_text = models.CharField(max_length=40,  null=True, blank=True)
    sentence_start_date = models.DateTimeField('date of sentence start', null=True, blank=True)
    sentence_stop_date = models.DateTimeField('date of sentence stop', null=True, blank=True)
    fine_amount = models.IntegerField(default=0,  null=True, blank=True)
    def __str__(self):
        return self.causeNumber
