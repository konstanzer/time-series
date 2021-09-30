# -*- coding: utf-8 -*-
"""time_series_acquire.ipynb
Generated with help from by Colaboratory.
Original file is located at
    https://colab.research.google.com/drive/13RIsusQUOAuYo93k57x91lr-cNg11YD3
"""

import requests
import pandas as pd


def return_df(url, df_name):
  data = requests.get(url + df_name).json()

  if df_name == 'sales':
    pages = data['payload']['max_page']
    df = pd.DataFrame(data['payload'][df_name])

    for p in range(2, pages+1):
      url2 = url + df_name + f'?page={p}'
      data = requests.get(url2).json()
      df = pd.concat([df, pd.DataFrame(data['payload'][df_name])])
  
  else:
    df = pd.DataFrame(data['payload'][df_name])

  return df


if __name__ == "__main__":

  url = 'https://python.zgulde.net/api/v1/'
  url2 =  'https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv'

  df_items = return_df(url, 'items')
  #next line takes about 5 minutes
  df_sales = return_df(url, 'sales') 
  df_stores = return_df(url, 'stores')

  #so id column matches column in sales
  df_stores.rename(columns={'store_id':'store'}, inplace=True)
  df_items.rename(columns={'item_id':'item'}, inplace=True)
  df_sales.rename(columns={'sale_id':'sale'}, inplace=True)

  df = df_sales.merge(df_stores)
  df = df.merge(df_items)

  print(df.head())
  print(df.shape)

  #save to drive (61 MB)
  df.to_csv('codeup_sales', index=False)

  """Open Power Systems Data for Germany includes country-wide totals
   of electricity consumption, wind power production, and solar power
   production for 2006-2017."""

  df2 = pd.read_csv(url2)
  
  print(df2.head())
  print(df2.shape)

  #save to drive (200 KB)
  df2.to_csv('codeup_power', index=False)

