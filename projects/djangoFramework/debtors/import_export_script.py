import tablib
from import_export import resources
from debtors.models import Debtor, Crime

crime_resource = resources.modelresource_factory(model=Crime)()
debtor_resource = resources.modelresource_factory(model=Debtor)()


datafile = ('/Users/rramsey32/Documents/bexar-db-final-ids.csv')

dry = False
dataset = tablib.Dataset().load(open(datafile).read())
result1 = debtor_resource.import_data(dataset, dry_run=dry)
#result3 = crime_resource.import_data(dataset, dry_run=dry)
#print(result2.has_errors())