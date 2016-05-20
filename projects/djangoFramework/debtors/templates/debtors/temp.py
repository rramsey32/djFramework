import pandas as pd
from debtors.models import Debtor, Crime
from django.contrib.auth.models import User
import datetime

td = pd.read_csv('C:\\Users\\rrams\\Desktop\\bexar-db-final-headers.csv')
td.to_csv('C:\\Users\\rrams\\Desktop\\bexar-tmp.csv', index=True, index_label="ID")
zz = pd.read_csv('C:\\Users\\rrams\\Desktop\\bexar-tmp.csv')

crimes_to_save = []

for row in zz['ID']:

    db = Crime(
            debtor = Debtor(debtor_name = zz.ix[row]['debtor_name']),
            causeNumber = zz.ix[row]['CASE-CAUSE-NBR'],
            sex = zz.ix[row]['SEX'],
            race = zz.ix[row]['RACE'],
            dob = datetime.date(zz.ix[row]['BIRTHDATE']),
            offense_date = datetime.date(zz.ix[row]['OFFENSE-DATE']),
            offense_text = zz.ix[row]['OFFENSE-DESC'],
            offense_type = zz.ix[row]['OFFENSE-TYPE'],
            case_text = zz.ix[row]['CASE-DESC'],
            disposition_text = zz.ix[row]['DISPOSITION-DESC'],
            judgement_date = datetime.date(zz.ix[row]['JUDGEMENT-DATE']),
            judgement_text = zz.ix[row]['JUDGEMENT-DESC'],
            sentence_text = zz.ix[row]['SENTENCE-DESC'],
            sentence_start_date = datetime.date(zz.ix[row]['SENTENCE-START-DATE']),
            sentence_stop_date = datetime.date(zz.ix[row]['SENTENCE-STOP-DATE']),
            fine_amount = int(zz.ix[row]['FINE-AMOUNT'])
        )
    crimes_to_save.append(db)

#Debtor.objects.bulk_create(crimes_to_save)

