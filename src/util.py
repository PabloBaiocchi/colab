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

def merge(list1,list2):
  mergeList=[]
  for i in range(len(list1)):
    mergeList.append(list1[i]+list2[i])
  return mergeList
