import datetime
from haystack import indexes
from debtors.models import Debtor, Crime

class DebtorIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    debtor_name = indexes.CharField(model_attr='debtor_name')

    def get_model(self):
        return Debtor

    def index_queryset(self, using=None):
        return self.get_model().objects.filter()

class CrimeIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    #causeNumber = indexes.CharField(model_attr='causeNumber')
    address = indexes.CharField(model_attr='address')
    city = indexes.CharField(model_attr='city')
    zip = indexes.CharField(model_attr='zip')

    def get_model(self):
        return Crime

    def index_queryset(self, using=None):
        return self.get_model().objects.filter()
