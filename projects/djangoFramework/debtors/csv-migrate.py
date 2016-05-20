import pandas as pd
from debtors.models import Debtor
from django.contrib.auth.models import User

td = pd.read_csv('C:\\Users\\rrams\\Desktop\\bexar-db-final-headers.csv')
td.to_csv('C:\\Users\\rrams\\Desktop\\bexar-tmp.csv', index=True, index_label="ID")
zz = pd.read_csv('C:\\Users\\rrams\\Desktop\\bexar-tmp.csv')

debtors_to_save = []

for row in zz['ID']:

    db = Debtor(
            debtor_name=zz.ix[row]['debtor_name'],
            debtor_address = zz.ix[row]['debtor_address'],
            debtor_city = zz.ix[row]['debtor_city'],
            debtor_state = zz.ix[row]['debtor_state'],
            debtor_zip = zz.ix[row]['debtor_zip'],
            debtor_phone = " ",
            debtor_added_by = User.objects.get_by_natural_key("admin")
        )
    debtors_to_save.append(db)


Debtor.objects.bulk_create(debtors_to_save)
