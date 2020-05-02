def callProfitFunction(strikePrice,optionPremium):
  def profitFunction(spotPrice):
    if spotPrice>strikePrice:
      return spotPrice-strikePrice-optionPremium
    return -optionPremium
  return profitFunction

def putProfitFunction(strikePrice,optionPremium):
  def profitFunction(spotPrice):
    if spotPrice<strikePrice:
      return strikePrice-spotPrice-optionPremium
    return -optionPremium 
  return profitFunction

def callProfit(spotPrice,strikePrice,optionPremium):
    if spotPrice>strikePrice:
      return spotPrice-strikePrice-optionPremium
    return -optionPremium

def putProfit(spotPrice,strikePrice,optionPremium):
    if spotPrice<strikePrice:
      return strikePrice-spotPrice-optionPremium
    return -optionPremium 

def constant(constantValue):
    def constantFunction(spotPrice):
        return constantValue
    return constantFunction

def apply(profitFunction,spotPrices):
    profits=[]
    for spotPrice in spotPrices:
        profits.append(profitFunction(spotPrice))
    return profits
