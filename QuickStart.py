import sqlite3
import os
import pandas as pd
from jj_data_connector.ga4 import GA4Report, Metrics, Dimensions

#Downloaded from GA API, link here: 
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials.json'

#Look on GA and see your property ID
property_id = 'YOUR-GA-4-ID'

# creating GA4Report object instance
ga4 = GA4Report(property_id)

# variables
dimension_list = ['date', 'browser', 'city']
metric_list = ['totalUsers', 'bounceRate','sessions']
date_range1 = ('2022-01-01', '2023-03-31')


# run the GA4 report
report = ga4.run_report(
    dimension_list, 
    metric_list, 
    date_ranges=[date_range1],
    row_limit=10,
    offset_row=10
)

report['row_count']

# report.keys()
print(report['response'])

report['headers']
report['rows']
df = pd.DataFrame(columns=report['headers'], data=report['rows'])
print(df)

# export to CSV and Excel files
df.to_csv('demo1.csv', index=False)
df.to_excel('demo1.xlsx', index=False)

# dataframe to SQL Server

conn = sqlite3.connect(r"C:\Users\Daniel\Desktop\GA$ API\datanase.db") 

df.to_sql('Analytics123', conn, if_exists='replace', index=False)

pd.read_sql('select * from Analytics123', conn)
