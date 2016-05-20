import pandas as pd
from debtor.models import Debtor, Crime
import datetime

td = pd.read_csv('C:\\Users\\rrams\\Desktop\\bexar-db-final-headers.csv')
td.to_csv('C:\\Users\\rrams\\Desktop\\bexar-tmp.csv', index=True, index_label="ID")
zz = pd.read_csv('C:\\Users\\rrams\\Desktop\\bexar-tmp.csv')

crimes_to_save = []

for row in zz['ID']:
    cElements = []
    debtor = Debtor(debtor_name = zz.ix[row]['debtor_name'])
    causeNumber = zz.ix[row]['CASE-CAUSE-NBR']
    sex = zz.ix[row]['SEX']
    race = zz.ix[row]['RACE']
    cElements.extend((debtor, causeNumber, sex, race))
    datb = zz.ix[row]['BIRTHDATE']
    if datb.isspace() == False:
        tokens = datb.split("/")
        year = int(tokens[2])
        if year < 8:
            year = str(year)
            if len(year) < 2:
                year = "0" + year
            year = "20" + str(year)
        else:
            year = "19" + str(year)
        dob = datetime.date(int(year), int(tokens[0]), int(tokens[1]))
        cElements.append(dob)
    fense_date = zz.ix[row]['OFFENSE-DATE']
    if fense_date.isspace() == False:
        tokens = fense_date.split("/")
        year = int(tokens[2])
        if year < 20:
            year = str(year)
            if len(year) < 2:
                year = "0" + year
            year = "20" + str(year)
            print(year)
        else:
            year = "19" + str(year)
        offense_date = datetime.date(int(year), int(tokens[0]), int(tokens[1]))
        cElements.append(offense_date)
    offense_text = zz.ix[row]['OFFENSE-DESC']
    offense_type = zz.ix[row]['OFFENSE-TYPE']
    case_text = zz.ix[row]['CASE-DESC']
    disposition_text = zz.ix[row]['DISPOSITION-DESC']
    cElements.extend((offense_text, offense_type, case_text, disposition_text))
    jment_date = zz.ix[row]['JUDGEMENT-DATE']
    if jment_date.isspace() == False:
        tokens = jment_date.split("/")
        year = int(tokens[2])
        if year < 20:
            year = str(year)
            if len(year) < 2:
                year = "0" + year
            year = "20" + str(year)
            print(year)
        else:
            year = "19" + str(year)
        judgement_date = datetime.date(int(year), int(tokens[0]), int(tokens[1]))
#        cElements.append(judgement_date)
    judgement_text = zz.ix[row]['JUDGEMENT-DESC']
    sentence_text = zz.ix[row]['SENTENCE-DESC']
    cElements.extend((judgement_text, sentence_text))
    sstrt_date = zz.ix[row]['SENTENCE-START-DATE']
    if sstrt_date.isspace() == False:
        tokens = sstrt_date.split("/")
        year = int(tokens[2])
        if year < 20:
            year = str(year)
            if len(year) < 2:
                year = "0" + year
            year = "20" + str(year)
            print(year)
        else:
            year = "19" + str(year)
        sentence_start_date = datetime.date(int(year), int(tokens[0]), int(tokens[1]))
#        cElements.append(sentence_start_date)
    sstp_date = zz.ix[row]['SENTENCE-END-DATE']
    if sstp_date.isspace() == False:
        tokens = sstp_date.split("/")
        year = int(tokens[2])
        if year < 20:
            year = str(year)
            if len(year) < 2:
                year = "0" + year
            year = "20" + str(year)
            print(year)
        else:
            year = "19" + str(year)
        sentence_stop_date = datetime.date(int(year), int(tokens[0]), int(tokens[1]))
        #cElements.append(sentence_stop_date)
    #fine_amount = 0
    #cElements.append(fine_amount)
    print(cElements)
    thisCrime = Crime(cElements)
    count = 0
    if count < 10:
        Crime.objects.create(thisCrime)
        count +=1
    print("ok")
    crimes_to_save.append(thisCrime)
    print("append ok")

#Crime.objects.bulk_create(crimes_to_save)


"""
    #sex = zz.ix[row]['SEX']
    #race = zz.ix[row]['RACE']
    #cElements.extend((debtor, causeNumber, sex, race))
    datb = zz.ix[row]['BIRTHDATE']
    if datb.isspace() == False:
        tokens = datb.split("/")
        year = int(tokens[2])
        if year < 8:
            year = str(year)
            if len(year) < 2:
                year = "0" + year
            year = "20" + str(year)
        else:
            year = "19" + str(year)
        dob = datetime.date(int(year), int(tokens[0]), int(tokens[1]))
    #    cElements.append(dob)
    fense_date = zz.ix[row]['OFFENSE-DATE']
    if fense_date.isspace() == False:
        tokens = fense_date.split("/")
        year = int(tokens[2])
        if year < 20:
            year = str(year)
            if len(year) < 2:
                year = "0" + year
            year = "20" + str(year)
            print(year)
        else:
            year = "19" + str(year)
        offense_date = datetime.date(int(year), int(tokens[0]), int(tokens[1]))
     #   cElements.append(offense_date)
    offense_text = zz.ix[row]['OFFENSE-DESC']
    offense_type = zz.ix[row]['OFFENSE-TYPE']
    case_text = zz.ix[row]['CASE-DESC']
    disposition_text = zz.ix[row]['DISPOSITION-DESC']
    #cElements.extend((offense_text, offense_type, case_text, disposition_text))
    jment_date = zz.ix[row]['JUDGEMENT-DATE']
    if jment_date.isspace() == False:
        tokens = jment_date.split("/")
        year = int(tokens[2])
        if year < 20:
            year = str(year)
            if len(year) < 2:
                year = "0" + year
            year = "20" + str(year)
            print(year)
        else:
            year = "19" + str(year)
        judgement_date = datetime.date(int(year), int(tokens[0]), int(tokens[1]))
#        cElements.append(judgement_date)
    judgement_text = zz.ix[row]['JUDGEMENT-DESC']
    sentence_text = zz.ix[row]['SENTENCE-DESC']
    #cElements.extend((judgement_text, sentence_text))
    sstrt_date = zz.ix[row]['SENTENCE-START-DATE']
    if sstrt_date.isspace() == False:
        tokens = sstrt_date.split("/")
        year = int(tokens[2])
        if year < 20:
            year = str(year)
            if len(year) < 2:
                year = "0" + year
            year = "20" + str(year)
            print(year)
        else:
            year = "19" + str(year)
        sentence_start_date = datetime.date(int(year), int(tokens[0]), int(tokens[1]))
#        cElements.append(sentence_start_date)
    sstp_date = zz.ix[row]['SENTENCE-END-DATE']
    if sstp_date.isspace() == False:
        tokens = sstp_date.split("/")
        year = int(tokens[2])
        if year < 20:
            year = str(year)
            if len(year) < 2:
                year = "0" + year
            year = "20" + str(year)
            print(year)
        else:
            year = "19" + str(year)
        sentence_stop_date = datetime.date(int(year), int(tokens[0]), int(tokens[1]))
        #cElements.append(sentence_stop_date)
    #fine_amount = 0
    #cElements.append(fine_amount)
"""

