import datetime as dt
import matplotlib.pyplot as plt
import numpy as np

from config import optionExpirationDates
from util import firstLastDigit,apply,constantFunction

def callProfit(spotPrice,strikePrice,optionPremium,percent=False):
    profit=0
    if spotPrice>strikePrice:
      profit=spotPrice-strikePrice-optionPremium
    else:
      profit=-optionPremium
    if percent:
      return profit/optionPremium
    return profit

def putProfit(spotPrice,strikePrice,optionPremium,percent=False):
    profit=0
    if spotPrice<strikePrice:
      profit=strikePrice-spotPrice-optionPremium
    else:
      profit=-optionPremium 
    if percent:
      return profit/optionPremium
    return profit
    

def optionProfit(spotPrice,strikePrice,premium,oType,percent=False):
  if oType=='call':
    return callProfit(spotPrice,strikePrice,premium,percent)
  if oType=='put':
    return putProfit(spotPrice,strikePrice,premium,percent)

def callProfitFunction(strikePrice,optionPremium,percent=False):
    def func(spotPrice):
        return callProfit(spotPrice,strikePrice,optionPremium,percent)
    return func

def putProfitFunction(strikePrice,optionPremium,percent=False):
    def func(spotPrice):
        return putProfit(spotPrice,strikePrice,optionPremium,percent)
    return func

def profitFunction(strikePrice,optionPremium,oType,percent=False):
    if oType=='call':
        return callProfitFunction(strikePrice,optionPremium,percent)
    if oType=='put':
        return putProfitFunction(strikePrice,optionPremium,percent)

def nyPriceFunction(ratio,baPrice):
  def function(ccl):
    return baPrice*ratio/ccl
  return function

def callBreakEven(strikePrice,premium):
  return strikePrice+premium

def putBreakEven(strikePrice,premium):
  return strikePrice-premium

def getBreakEven(strikePrice,premium,oType):
  if oType=='call':
    return callBreakEven(strikePrice,premium)
  if oType=='put':
    return putBreakEven(strikePrice,premium)

def getExpirationDate(optionName):
  month=optionName[-2:]
  return dt.datetime.strptime(optionExpirationDates[month],'%Y-%m-%d')

def getStrikePrice(optionName):
  firstDigitIndex, lastDigitIndex=firstLastDigit(optionName)
  return float(optionName[firstDigitIndex:lastDigitIndex+1])

def getType(optionName):
  indexes=firstLastDigit(optionName)
  if optionName[indexes[0]-1]=='C':
    return 'call'
  if optionName[indexes[0]-1]=='V':
    return 'put'

def fillOut(optionsDf):
  optionsDf['exp_date']=optionsDf.name.apply(lambda x:getExpirationDate(x))
  optionsDf['strike_price']=optionsDf.name.apply(lambda x:getStrikePrice(x))
  optionsDf['type']=optionsDf.name.apply(lambda x:getType(x))
  optionsDf['break_even']=optionsDf.apply(lambda row:getBreakEven(row['strike_price'],row['premium'],row['type']),axis=1)
  optionsDf['exp_month']=optionsDf.exp_date.apply(lambda x: x.month)
  optionsDf['datetime']=optionsDf.datetime.apply(lambda datestring: dt.datetime.strptime(datestring[:datestring.rindex(':')],'%Y-%m-%d %H:%M'))

def graph(optionsDf,figsize=(20,13),start=0,stop=200,percent=False):
  plt.figure(figsize=figsize)

  spotPrices=np.linspace(start,stop,stop-start)

  for row in optionsDf.iterrows():
    strikePrice=row[1].strike_price
    premium=row[1].premium
    oType=row[1].type
    name=row[1][0]
    profitFunc=profitFunction(strikePrice,premium,oType,percent)
    profit=apply(profitFunc,spotPrices)
    plt.plot(spotPrices,profit,label=name)
  
  plt.plot(spotPrices,apply(constantFunction(0),spotPrices),c='black')
  
  plt.legend()
  plt.grid()

def graphCombined(optionsDf,figsize=(20,13),start=0,stop=200,percent=False):
  plt.figure(figsize=figsize)

  spotPrices=np.linspace(start,stop,stop-start)
  grossProfit=np.array([0] * len(spotPrices))
  totalPremium=0

  for row in optionsDf.iterrows():
    strikePrice=row[1].strike_price
    premium=row[1].premium
    totalPremium=totalPremium+premium
    oType=row[1].type
    profitFunc=profitFunction(strikePrice,premium,oType)
    optionProfit=np.array(apply(profitFunc,spotPrices))
    grossProfit=grossProfit+optionProfit
  
  if percent:
    plt.plot(spotPrices,grossProfit/totalPremium)
  else:
    plt.plot(spotPrices,grossProfit)
  plt.plot(spotPrices,apply(constantFunction(0),spotPrices),c='black')

  plt.grid()