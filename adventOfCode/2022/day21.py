from copy import deepcopy

from utility import *

day=21

def simpleOperation(op1, op2, opSymbol):
  if(opSymbol=="+"):
    return op1+op2
  if(opSymbol=="-"):
    return op1-op2
  if(opSymbol=="/"):
    return op1/op2
  if(opSymbol=="*"):
    return op1*op2

def updateNotKnownVariable(name, value, notKnownVariables):
  elementsToUpdate=[]
  for key, element in notKnownVariables.items():
    found=False
    if(element["operando1"]==name):
      element["operando1"]=value
      found=True
    if(element["operando2"]==name):
      element["operando2"]=value
      found=True
    if(found and (isinstance(element["operando1"], int) or isinstance(element["operando1"], float)) and (isinstance(element["operando2"], int) or isinstance(element["operando2"], float))):
      elementsToUpdate.append((key, simpleOperation(element["operando1"], element["operando2"], element["operazione"])))

  return elementsToUpdate
      
      
def updateKnownVariable(name, value, knownVariables, notKnownVariables):
  knownVariables[name]=value
  elementsToUpdate=updateNotKnownVariable(name,  value, notKnownVariables)
  return elementsToUpdate


def comprehension(rows, part):
  knownVariables=dict()
  notKnownVariables=dict()

  for row in rows:
    splitted=row.replace(":","").split(" ")
    if(splitted[0]=="humn" and part=="b"):
      continue
    if(len(splitted)==2):
      knownVariables[splitted[0]]=int(splitted[1])
      elementsToUpdate=updateNotKnownVariable(splitted[0], int(splitted[1]), notKnownVariables)
      while(len(elementsToUpdate)>0):
        element=elementsToUpdate.pop(0)
        elementsToUpdate=elementsToUpdate+updateKnownVariable(element[0], element[1], knownVariables, notKnownVariables)
    if(len(splitted)==4):
      operando1=splitted[1]
      operazione=splitted[2]
      operando2=splitted[3]
      if(operando1 in knownVariables):
        operando1=knownVariables[operando1]
      if(operando2 in knownVariables):
        operando2=knownVariables[operando2]

      if((isinstance(operando1, int) or isinstance(operando1, float)) and (isinstance(operando2, int) or isinstance(operando2, float))):
        elementsToUpdate=updateKnownVariable(splitted[0], simpleOperation(operando1, operando2, operazione), knownVariables, notKnownVariables)

        while(len(elementsToUpdate)>0):
          element=elementsToUpdate.pop(0)
          elementsToUpdate=elementsToUpdate+updateKnownVariable(element[0], element[1], knownVariables, notKnownVariables)        

      else:
        notKnownVariables[splitted[0]]=dict(operando1=operando1, operazione=operazione, operando2=operando2)  
  return knownVariables, notKnownVariables

def checkSample(sample, numberToFind, knownVariables, notKnownVariables):
  elementsToUpdate=updateKnownVariable("humn", sample, knownVariables, notKnownVariables)
  while(len(elementsToUpdate)>0):
    element=elementsToUpdate.pop(0)
    elementsToUpdate=elementsToUpdate+updateKnownVariable(element[0], element[1], knownVariables, notKnownVariables)     
  return knownVariables["root"]-numberToFind

def solve1():
  rows=getOldAocInput(day)
  knownVariables, _=comprehension(rows, "a")

  return int(knownVariables["root"])

def solve2():
  rows=getOldAocInput(day)
  knownVariables, notKnownVariables=  comprehension(rows, "b")

  if(isinstance(notKnownVariables["root"]["operando1"],int) or isinstance(notKnownVariables["root"]["operando1"],float)):
    numberToFind=notKnownVariables["root"]["operando1"]
  if(isinstance(notKnownVariables["root"]["operando2"], int) or isinstance(notKnownVariables["root"]["operando2"], float)):
    numberToFind=notKnownVariables["root"]["operando2"]

  numberToFind=numberToFind*2

  sample=0

  result0=checkSample(sample, numberToFind, deepcopy(knownVariables), deepcopy(notKnownVariables.copy()))
  if(result0==0):
    return sample

  sample=sample+1
  result1=checkSample(sample, numberToFind, deepcopy(knownVariables), deepcopy(notKnownVariables.copy()))
  if(result1==0):
    return sample

  if(result1-result0>0):
    isToSwap=-1
  else:
    isToSwap=1

  foundMax=0
  foundMin=0 

  while(True):
    if(foundMax==0):
      sample=sample*2
    if(foundMax!=0):
      if ((foundMax-foundMin)%2==1):
        foundMax=foundMax+1
      halfDirection=(foundMax-foundMin)//2
      sample=foundMin+halfDirection

    # print("check", foundMin, sample, foundMax, end="")
    result=checkSample(sample, numberToFind, deepcopy(knownVariables), deepcopy(notKnownVariables.copy()))
    # print(" ", result)
    if((isToSwap*result)>0):
      foundMin=sample
    if((isToSwap*result)<0):
      foundMax=sample
    if(result==0):
      return sample


print(solve1())
print(solve2())