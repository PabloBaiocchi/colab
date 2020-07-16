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
    df['compra']=df['compra'].apply(lambda x: convertToFloat(x))
    df['venta']=df['venta'].apply(lambda x: convertToFloat(x))
    return df