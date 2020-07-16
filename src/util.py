import datetime as dt

def constantFunction(constantValue):
    def function(value):
        return constantValue
    return function

def apply(function,inputs):
    outputs=[]
    for val in inputs:
        outputs.append(function(val))
    return outputs

def firstLastDigit(myString):
  firstInstance=-1
  lastInstance=-1
  for i,c in enumerate(myString):
    if c.isdigit():
      if firstInstance<0:
        firstInstance=i
      else:
        lastInstance=i
  return firstInstance,lastInstance

def splitDatetime(df):
  df['date']=df.datetime.apply(lambda timestamp: timestamp.date())
  df['minutes']=df.datetime.apply(lambda timestamp: timestamp.hour*60+timestamp.minute)

def convertToFloat(numString):
  return float(numString.replace(',','.')) 

balanzScrapeFileColumns=['ticker','plazo','max','min','open','last_op','total_volume','datetime','cc0','cc1','cc2','cc3','cc4','cv0','cv1','cv2','cv3','cv4','pc0','pc1','pc2','pc3','pc4','pv0','pv1','pv2','pv3','pv4']