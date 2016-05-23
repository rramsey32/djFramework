import pandas as pd

file_prefix = "/Users/rramsey32/Documents/"
td = pd.read_csv(file_prefix + "bexar-db-final.csv")
outfile = file_prefix + "bexar-indexed-data.csv"
td.to_csv(outfile, index=True, index_label="ID")