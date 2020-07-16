import pandas as pd
import datetime as dt
import requests

from util import convertToFloat

def getDollarMayoristaJson(start_date,end_date):
    date_format='%d-%m-%Y'
    url=f"https://mercados.ambito.com//dolar/mayorista/historico-general/{start_date.strftime(date_format)}/{end_date.strftime(date_format)}"
    session=requests.session()
    return session.get(url).json()

def getDollarMayoristaFrame(startDate=dt.date(2019,12,10),endDate=dt.date.today()):
    prices=getDollarMayoristaJson(startDate,endDate)[1:]
    df=pd.DataFrame(prices)
    df.columns=['date','compra','venta']
    df['date']=pd.to_datetime(df.date,format='%d-%m-%Y')
    df['compra']=df['compra'].apply(lambda x: convertToFloat(x))
    df['venta']=df['venta'].apply(lambda x: convertToFloat(x))
    return df

def getLatestPrice(ticker,frame):
    tempDf=frame[frame.ticker==ticker]
    return tempDf[tempDf.datetime==tempDf.datetime.max()].iloc[0].last_op

def getLatestDollarMayoristaFutures(frame):
    rows=[]
    for ticker in frame.ticker.unique():
        if ticker[0:2]=='DO' and ticker[-1]=='A':
            rows.append([ticker,getLatestPrice(ticker,frame)])
    df=pd.DataFrame(rows)
    df.columns=['ticker','price']
    df['expiration_date']=df.ticker.apply(lambda x: rofexExpirations[x[2:-1]])
    return df

rofexExpirations={
    'Jun20':dt.date(2020,6,30),
    'Jul20':dt.date(2020,7,31),
    'Ago20':dt.date(2020,8,31),
    'Sep20':dt.date(2020,9,30),
    'Oct20':dt.date(2020,10,30),
    'Nov20':dt.date(2020,11,27),
    'Dic20':dt.date(2020,12,30),
    'Ene21':dt.date(2021,1,29),
    'Feb21':dt.date(2021,2,26),
    'Mar21':dt.date(2021,3,31),
    'Abr21':dt.date(2021,4,30),
    'May21':dt.date(2021,5,31),
    'Jun21':dt.date(2021,6,30)
}