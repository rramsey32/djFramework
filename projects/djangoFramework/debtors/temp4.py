import pandas as pd
from debtors.models import Debtor, Crime
import datetime

#td = pd.read_csv('C:\\Users\\rrams\\Desktop\\bexar-db-final-headers.csv')
#td.to_csv('C:\\Users\\rrams\\Desktop\\bexar-tmp.csv', index=True, index_label="ID")
print("hello")
zz = pd.read_csv('C:\\Users\\rrams\\Desktop\\bexar-tmp.csv')

print("hello")
for row in zz['ID']:
    cElements = []
    d = zz.ix[row]['debtor_name']
    d = d.strip()
    debtor = Debtor(d)
    causeNumber = zz.ix[row]['CASE-CAUSE-NBR']
    causeNumber = causeNumber.strip()
