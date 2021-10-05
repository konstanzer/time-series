import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt

"""Exercises 3: Prepare"""

def datetime_index(df, colname):
	'''
	Make datetime index
	'''
	df[colname] = pd.to_datetime(df[colname])
	df.set_index(colname, inplace=True)

	return df

def day_year_month(df):
	'''
	Add day and month column fromd datetime index.
	'''
	df['month'] = df.index.month_name()
	df['year'] = df.index.year
	df['weekday'] = df.index.day_name()

	return df

def see_distributions(df):
	'''
	Plot histograms for all variables.
	'''
	for x in df.columns:
	  plt.hist(df[x])
	  plt.xlabel(x)
	  plt.show()

def fillnanmedian(df):
	'''
	Fill what columns you can with median.
	'''
	for x in df.columns:
	  try:
	    df[x] = df[x].fillna(np.nanmedian(df[x]))
	  except:
	    pass

	return df


if __name__ == "__main__":

	#Store data
	df = pd.read_csv('codeup_sales').sample(100000)

	df['sales_total'] = df.item_price * df.sale_amount
	df = datetime_index(df, 'sale_date')
	df = day_and_month(df)

	#Germany Power Data
	df = pd.read_csv(PATH + 'codeup_power')

	df = datetime_index(df, 'Date')
	df = fillnanmedian(df)

