from django.db import models
from django.contrib.auth.models import User
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
    debtor_name = models.CharField(max_length=100)
    debtor_address = models.CharField(max_length=200)
    debtor_city = models.CharField(max_length=50)
    debtor_state = models.CharField(max_length=2)
    debtor_zip = models.CharField(max_length=15)
    debtor_phone = models.CharField(max_length=25)
    debtor_added_by = models.ForeignKey(User)
    def __str__(self):
        return self.debtor_name
    def get_absolute_url(self):
        return "/debtors/%i/" % self.id

class Debt(models.Model):
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE)
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
    debtor = models.ForeignKey(Debtor, on_delete=models.CASCADE)
    causeNumber = models.CharField(max_length = 15)
    sex = models.CharField(max_length=1)
    race = models.CharField(max_length=3)
    myDate = timezone.now()
    dob = models.DateTimeField('date of birth', default=myDate)
    offense_date = models.DateTimeField('date of offense', default=myDate)
    offense_text = models.CharField(max_length=100, default="MM")
    offense_type = models.CharField(max_length=10, default="MM")
    case_text = models.CharField(max_length=20, default="MM")
    disposition_text = models.CharField(max_length=40, default="MM")
    judgement_date = models.DateTimeField('date of judgement', default=myDate)
    judgement_text = models.CharField(max_length=40, default="MM")
    sentence_text = models.CharField(max_length=40, default="MM")
    sentence_start_date = models.DateTimeField('date of sentence start', default=myDate)
    sentence_stop_date = models.DateTimeField('date of sentence stop', default=myDate)
    fine_amount = models.IntegerField(default=0)
    def __str__(self):
        return self.causeNumber