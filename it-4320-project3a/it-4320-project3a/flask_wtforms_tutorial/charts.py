'''
This web service extends the Alphavantage api by creating a visualization module, 
converting json query results retuned from the api into charts and other graphics. 

This is where you should add your code to function query the api
'''
import requests
from datetime import datetime
from datetime import date
import time
#import alpha_vantage-> DOES NOT WANT TO IMPORT FOR SOME REASON?!
#from alpha_vantage.timeseries import TimeSeries -> DOES NOT WANT TO IMPORT FOR SOME REASON?!
import pygal
#import pandas as pd -> DOES NOT WANT TO IMPORT FOR SOME REASON?!


#queries.json()

API_URL = "https://www.alphavantage.co/query"
API_KEY = "X0AWJSYKTOKX2F5E"

def getData(stock_symbol, time_series, chart_type, start_date, end_date):
    #temp fix to not crash the webapp
    time_Dict = { '1': 'TIME_SERIES_INTRADAY', '2': 'TIME_SERIES_DAILY', '3': 'TIME_SERIES_WEEKLY', '4': 'TIME_SERIES_MONTHLY'}
    time_choice = time_Dict[time_series]
    API_URL = "https://www.alphavantage.co/query"
    API_KEY = "X0AWJSYKTOKX2F5E"
    parameters = { 'function': time_choice,
                'symbol': stock_symbol,
                'interval': '60min',
                'outputsize': 'full',
                'apikey': API_KEY}

#    ts = TimeSeries(key=API_KEY, output_format='pandas')
#    if timeSeries == '1':
#        data, meta_data = ts.get_intraday(symbol=symbol, interval='60min', outputsize='full')
#        f = 'H'
#    if timeSeries == '2':
#        data, meta_data = ts.get_daily(symbol=symbol, outputsize='compact')
#        f = 'D'
#    if timeSeries == '3':
#        data, meta_data = ts.get_weekly(symbol=symbol)
#        f = 'W'
#    if timeSeries == '4':
#        data, meta_data = ts.get_monthly(symbol=symbol)
#        f = 'M'

    response = requests.get(API_URL, params=parameters)
    return response


    data_date_changed = data[end_date:start_date]

    if chart_type == "1":
        line_chart = pygal.Bar(x_label_rotation=20, width=1000, height = 400)
        line_chart.title = 'Stock Data for {}:  {} to {}'.format(stock_symbol, start_date, end_date)
        labels = data_date_changed.index.to_list()
        line_chart.x_labels= reversed(labels)
        line_chart.add("Open", data_date_changed['1. open'])
        line_chart.add("High", data_date_changed['2. high'])
        line_chart.add("Low", data_date_changed['3. low'])
        line_chart.add("Close", data_date_changed['4. close'])
        line_chart.render()
        return line_chart

    elif chart_type == "2":
        line_chart = pygal.Line(x_label_rotation=20, width=1000, height = 400)
        line_chart.title = 'Stock Data for {}: {} to {}'.format(stock_symbol, start_date, end_date)
        labels = data_date_changed.index.to_list()
        line_chart.x_labels= reversed(labels)
        line_chart.add("Open", data_date_changed['1. open'])
        line_chart.add("High", data_date_changed['2. high'])
        line_chart.add("Low", data_date_changed['3. low'])
        line_chart.add("Close", data_date_changed['4. close'])
        line_chart.render()
        return line_chart

#Helper function for converting date
def convert_date(str_date):
    return datetime.strptime(str_date, '%Y-%m-%d').date()

