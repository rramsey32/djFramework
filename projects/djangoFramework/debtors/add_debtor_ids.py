# this script takes our bexar county csv and adds a unique debtor id field
#import pandas as pd
import csv

datafile = ('/Users/rramsey32/Documents/bexar-db-final.csv')
outfile = ('/Users/rramsey32/Documents/bexar-db-final-ids.csv')
of = open(outfile, 'w')
#df = open(datafile, 'r')

lastDebtor = ""
lastID = 1
count = 0


print("Going to open in and out files...")

with open(datafile) as csvfile:
        fileReader = csv.reader(csvfile,delimiter=',', quotechar='"')
        for row in fileReader:
            newline = ""

            if count == 0:
                print("first line in loop. should not see this message again")
                newline = "debtor_id," + ','.join(row)
                count += 1
            elif count == 1:
                currentDebtor = row[1]
                row[1] = "\"" + row[1] + "\""
                row[2] = "\"" + row[2] + "\""
                row[3] = "\"" + row[3] + "\""
                row[11] = "\"" + row[11] + "\""
                row[16] = "\"" + row[16] + "\""
                line = ",".join(row)
                newline = "1," + line
                lastDebtor = currentDebtor
                count += 1
                print("going to write line: ", newline)
            else:
                currentDebtor = row[1]
                row[1] = "\"" + row[1] + "\""
                row[2] = "\"" + row[2] + "\""
                row[3] = "\"" + row[3] + "\""
                row[11] = "\"" + row[11] + "\""
                row[16] = "\"" + row[16] + "\""
                line = ",".join(row)
                if lastDebtor != currentDebtor:
                    lastID += 1
                    lastDebtor = currentDebtor
                newline = str(lastID) + "," + line
                if count < 10:
                    print(newline)
                    count += 1
            newline = newline + "\n"
            of.write(newline)
            of.flush()

of.close()