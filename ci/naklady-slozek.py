import pandas
import sys

pandas.read_excel(sys.argv[1]).to_csv(
    'naklady-slozek-2025.csv',
    sep=';',
    index=None, # no row numbers
    header=True)
