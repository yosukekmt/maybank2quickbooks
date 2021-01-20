import os
import sys
import json
import pandas as pd
from datetime import datetime

FILE_PATH = sys.argv[1]

def main():
    date_parser = lambda x: datetime.strptime(x, '%d/%b/%Y MY (UTC+08:00)')
    df = pd.read_csv(FILE_PATH, thousands=',', parse_dates=['Posting Date'], date_parser=date_parser)
    df["Date"]   = df['Posting Date'].apply(lambda x: x.strftime('%d/%m/%Y'))
    df["Description"] =  df['Transaction Description 2']
    df["Description"].fillna(df["Transaction Description 3"], inplace=True)
    df["Credit"] = pd.to_numeric(df['Credit'], errors='coerce').fillna(0)
    df["Debit"] =  pd.to_numeric(df['Debit'], errors='coerce').fillna(0)
    del df['Account Number']
    del df['Account Type']
    del df['Account Name']
    del df['Account Currency']
    del df['Date From']
    del df['Date To']
    del df['Total Debit']
    del df['Total Credit']
    del df['Begin Balance']
    del df['End Balance']
    del df['Transaction Date']
    del df['Transaction Time']
    del df['Posting Date']
    del df['Processing Time']
    del df['Transaction Description']
    del df['Transaction Ref']
    del df['Source Code']
    del df['Teller ID']
    del df['Branch/Channel']
    del df['Transaction Code']
    del df['End Balance.1']
    del df['Filler']
    del df['Virtual Account']
    del df['Transaction Description 2']
    del df['Transaction Description 3']
    del df['Transaction Description 4']
    del df['Expiry Date']
    print(df)
    df.to_csv('out.csv', index=False)


if __name__ == '__main__':
    main()
