import os
import requests
import numpy as np
import pandas as pd
import datetime

from helpers import parse_page

DATA_LOCATION = '../data/data.csv'

def main():
    url = 'https://www.einmalzahlung200.de/eppsg-de'
    # Get the page
    page = requests.get(url)
    status = page.status_code
    if status != 200:
        raise Exception('Could not get the page')

    parsed = parse_page(page)
    
    # create data object
    d = data()
    d.successful_count = parsed[0]
    d.succesful_timestamp = parsed[1]
    d.paid_out = parsed[2]
    d.paid_out_sum = parsed[3]
    d.paid_out_timestamp = parsed[4]

    # create folder if it does not exist
    if not os.path.exists('../data'):
        os.mkdir('../data')
        
    d.to_csv()

class data:
    def __init__(self):
        self.timestamp:datetime.datetime = datetime.datetime.now()
        self.successful_count:(np.int64 | None) = None
        self.succesful_timestamp:(datetime.datetime | None) = None
        self.paid_out:(np.int64 | None) = None
        self.paid_out_sum:(np.int64 | None) = None
        self.paid_out_timestamp:(datetime.datetime | None) = None

    def __str__(self):
        return f'{self.timestamp} | Anträge gestellt: {self.successful_count} ({self.succesful_timestamp}) | Anträge ausgezahlt: {self.paid_out}, Gesamt: {self.paid_out_sum}€ ({self.paid_out_timestamp})'
    
    def __dict__(self):
        return {
            'timestamp': self.timestamp,
            'successful_count': self.successful_count,
            'succesful_timestamp': self.succesful_timestamp,
            'paid_out': self.paid_out,
            'paid_out_sum': self.paid_out_sum,
            'paid_out_timestamp': self.paid_out_timestamp
        }

    def to_csv(self):
        df = pd.DataFrame([self.__dict__()])
        if not os.path.exists(DATA_LOCATION):
            df.to_csv(DATA_LOCATION, index=False)
        else:
            # check if the data is already in the csv
            df_csv = pd.read_csv(DATA_LOCATION)
            df_csv['succesful_timestamp'] = pd.to_datetime(df_csv['succesful_timestamp'])
            df_csv['paid_out_timestamp'] = pd.to_datetime(df_csv['paid_out_timestamp'])
            if self.succesful_timestamp in df_csv['succesful_timestamp'].values and self.paid_out_timestamp in df_csv['paid_out_timestamp'].values:
                print('Data is already in the csv. Skipping...')
                return
            pd.concat([pd.read_csv(DATA_LOCATION), df], ignore_index=True).to_csv(DATA_LOCATION, index=False)
        

if __name__ == '__main__':
    main()
