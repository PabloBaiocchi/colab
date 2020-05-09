import datetime as dt

from config import optionExpirationDates
from util import firstLastDigit

def callProfit(spotPrice,strikePrice,optionPremium):
    if spotPrice>strikePrice:
      return spotPrice-strikePrice-optionPremium
    return -optionPremium

def putProfit(spotPrice,strikePrice,optionPremium):
    if spotPrice<strikePrice:
      return strikePrice-spotPrice-optionPremium
    return -optionPremium 

def optionProfit(spotPrice,strikePrice,premium,oType):
  if oType=='call':
    return callProfit(spotPrice,strikePrice,premium)
  if oType=='put':
    return putProfit(spotPrice,strikePrice,premium)

def callProfitFunction(strikePrice,optionPremium):
    def func(spotPrice):
        return callProfit(spotPrice,strikePrice,optionPremium)
    return func

def putProfitFunction(strikePrice,optionPremium):
    def func(spotPrice):
        return putProfit(spotPrice,strikePrice,optionPremium)
    return func

def profitFunction(strikePrice,optionPremium,oType):
    if oType=='call':
        return callProfitFunction(strikePrice,optionPremium)
    if oType=='put':
        return putProfitFunction(strikePrice,optionPremium)

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