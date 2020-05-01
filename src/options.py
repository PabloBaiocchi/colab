def callProfit(strikePrice,optionPremium):
  def profitFunction(spotPrice):
    if spotPrice>strikePrice:
      return spotPrice-strikePrice-optionPremium
    return -optionPremium
  return profitFunction

def putProfit(strikePrice,optionPremium):
  def profitFunction(spotPrice):
    if spotPrice<strikePrice:
      return strikePrice-spotPrice-optionPremium
    return -optionPremium 
  return profitFunction

def constant(constantValue):
    def constantFunction(spotPrice):
        return constantValue
    return constantFunction

def apply(profitFunction,spotPrices):
    profits=[]
    for spotPrice in spotPrices:
        profits.append(profitFunction(spotPrice))
    return profits
