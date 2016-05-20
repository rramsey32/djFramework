import pandas as pd
from debtors.models import Debtor, Crime
import datetime


zz = pd.read_csv('C:\\Users\\rrams\\Desktop\\bexar-tmp.csv')

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
