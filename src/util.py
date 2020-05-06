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