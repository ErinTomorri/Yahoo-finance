import pandas as pd
import yfinance as yf
from yahoofinancials import YahooFinancials
import os  
yahoo_financials = YahooFinancials('TICKER')

data = yahoo_financials.get_historical_price_data(start_date='2022-04-12', 
                                                  end_date='2022-07-12', 
                                                  time_interval='daily')

tsla_df = pd.DataFrame(data['TICKER']['prices'])
tsla_df = tsla_df.drop('date', axis=1).set_index('formatted_date')
tsla_df.head()

os.makedirs('DATACSV', exist_ok=True)  
tsla_df.to_csv("DATACSV/Stock_Data.csv",index=True)
