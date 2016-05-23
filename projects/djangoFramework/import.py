import pandas as pd
from debtors.models import Debtor, Crime
import datetime

td = pd.read_csv('/Users/rramsey32/Documents/bexar-db-final-headers.csv')
td.to_csv('/Documents/rramsey32/Documents/bexar-tmp.csv', index=True, index_label="ID")
zz = pd.read_csv('/Documents/rramsey32/Documents/bexar-tmp.csv')

print("starting...")
for row in zz['ID']:
    cElements = []
    d = zz.ix[row]['debtor_name']
    d = d.strip()
    debtor = Debtor(d)
    causeNumber = zz.ix[row]['CASE-CAUSE-NBR']
    causeNumber = causeNumber.strip()
    cElements.append(debtor)
    cElements.append(causeNumber)
print("stop...")
