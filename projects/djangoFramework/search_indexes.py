import datetime
from haystack import indexes
from debtors.models import Debtor

class DebtorIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    debtor_name = indexes.CharField(model_attr='debtor_name')
    debtor_address = indexes.CharField(model_attr='debtor_address')
    debtor_phone = indexes.CharField(model_attr='debtor_phone')
    debtor_dob = indexes.DateField(model_attr='debtor_dob')
    debtor_city = indexes.CharField(model_attr='debtor_city')
    debtor_zip = indexes.CharField(model_attr='debtor_zip')

    def get_model(self):
        return Debtor

    def index_queryset(self, using=None):
        return self.get_model().objects.filter()
