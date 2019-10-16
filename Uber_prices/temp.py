import numpy as np
import pandas as pd

cab_df = pd.read_csv('./cab_rides.csv',encoding = "UTF-16")
weather_df = pd.read_csv('./weather.txt',encoding = "UTF-16")
cab_df['id'] = range(len(cab_df))
cab_df['date_time'] = pd.to_datetime((cab_df['time_stamp']/1000).astype(np.int64), unit='s')
weather_df['date_time'] = pd.to_datetime(weather_df['time_stamp'], unit='s')
cab_df['merge_date'] = cab_df.source.astype(str) +" - "+ cab_df.date_time.dt.date.astype("str") +" - "+ cab_df.date_time.dt.hour.astype("str") 
weather_df['merge_date'] = weather_df.location.astype(str) +" - "+ weather_df.date_time.dt.date.astype("str") +" - "+ weather_df.date_time.dt.hour.astype("str")
weather_df['rain'] = weather_df['rain'].fillna(0)
weather_df2 = weather_df.groupby('merge_date').apply(np.mean).reset_index(drop=False)

merged_df = pd.merge(cab_df,weather_df2,how='left',on=['merge_date'])
del merged_df['time_stamp_y']
del merged_df['time_stamp_x']
del merged_df['merge_date']

merged_df['Year'] = merged_df.date_time.dt.year
merged_df['Month'] = merged_df.date_time.dt.month
merged_df['Day'] = merged_df.date_time.dt.day
merged_df['Hour'] = merged_df.date_time.dt.hour
merged_df['Min'] = merged_df.date_time.dt.minute

merged_df.iloc[::7].to_csv('full.csv',index=0)
