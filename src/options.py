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

def constant(constantValue):
    def constantFunction(spotPrice):
        return constantValue
    return constantFunction

def apply(profitFunction,spotPrices):
    profits=[]
    for spotPrice in spotPrices:
        profits.append(profitFunction(spotPrice))
    return profits
