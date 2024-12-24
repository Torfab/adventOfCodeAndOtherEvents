from utilityz import *

# Not generic solution for part 2 but tailored on my input, it's a good error detection tho 
# After i detected an error I wrote the part of code that solved my input, i did it 4 times)

operators={
  "AND": lambda x,y: x and y,
  "OR": lambda x,y: x or y,
  "XOR": lambda x,y: x^y
}

def parseRows(rows):
  state="registers"
  registers={}
  operations=[]
  for row in rows:
    if row=="":
      state="operations"
      continue
    if state=="registers":
      rowSplitted=row.split(": ")
      registers[rowSplitted[0]]=int(rowSplitted[1])
    elif state=="operations":
      rowSplitted=row.split(" ")
      newItem={}
      if rowSplitted[2][0]=="x":
        newItem["firstOperand"]=rowSplitted[2]
        newItem["secondOperand"]=rowSplitted[0]
      else:
        newItem["firstOperand"]=rowSplitted[0]
        newItem["secondOperand"]=rowSplitted[2]
      newItem["operator"]=rowSplitted[1]
      newItem["targetRegister"]=rowSplitted[4]
      operations.append(newItem)

  return registers, operations

def solve():
  rows=getOldAocInput(24)
  registers, operations=parseRows(rows)

  queueOfOperations=operations
  while(len(queueOfOperations)>0):
    tryElement=0
    while(True):
      elementToTry=queueOfOperations[tryElement]
      if(registers.get(elementToTry["firstOperand"])!=None and registers.get(elementToTry["secondOperand"])!=None):
        break
      tryElement=tryElement+1
      
    operation=queueOfOperations.pop(tryElement)
    registerTarget=operation["targetRegister"]
    funcOperation=operators[operation["operator"]]
    firstOperand=registers.get(operation["firstOperand"])
    secondOperand=registers.get(operation["secondOperand"])
    registers[registerTarget]=funcOperation(firstOperand, secondOperand)

  arrayOfKeys=list(k for k in registers.keys() if k[0]=="z")
  arrayOfKeys.sort()

  ris=""
  for a in reversed(arrayOfKeys):
    ris=ris+str(registers[a])


  return fromBinaryToInteger(ris)


def startAnswer(start, operations):
  currentOperation=next((operation for operation in operations if operation["operator"]=="XOR" and operation["firstOperand"]=="x"+padNumberString(start)), None)
  if currentOperation["targetRegister"]!="z"+padNumberString(start):
    # print("Error Detected")
    return
  
  currentOperation=next((operation for operation in operations if operation["operator"]=="AND" and operation["firstOperand"]=="x"+padNumberString(start)), None)
  currentCarrier=currentOperation["targetRegister"]
  if currentCarrier[0]=="z":
    # print("Error Detected")
    return
  
  return currentCarrier

def padNumberString(num):
  num=str(num)
  if(len(num)==1):
    return "0"+num
  return num
  
def fixThingsWithZ(temp, operations, sumTemp,  currentOperation, carriersArray, currentIndex, risArray):
  tempIdx=int(temp[1:])
  if tempIdx==currentIndex:
    newCurrentOperation=next((operation for operation in operations if operation["operator"]=="XOR" and operation["firstOperand"]==carriersArray[currentIndex-1] and operation["secondOperand"]==sumTemp), None)
    if newCurrentOperation==None:
      newCurrentOperation=next((operation for operation in operations if operation["operator"]=="XOR" and operation["secondOperand"]==carriersArray[currentIndex-1] and operation["firstOperand"]==sumTemp), None)
    currentOperation["targetRegister"]=newCurrentOperation["targetRegister"]
    newCurrentOperation["targetRegister"]=temp

    risArray.append(currentOperation["targetRegister"])
    risArray.append(temp)
    return currentOperation["targetRegister"]
  elif (tempIdx==currentIndex+1):
    newCurrentOperation=next((operation for operation in operations if operation["operator"]=="XOR" and operation["firstOperand"]=="x"+padNumberString(currentIndex+1) and operation["secondOperand"]=="y"+padNumberString(currentIndex+1)), None)
    sumTemp=newCurrentOperation["targetRegister"]
    newCurrentOperation=next((operation for operation in operations if operation["operator"]=="XOR" and operation["firstOperand"]==sumTemp), None)
    if newCurrentOperation==None:
      newCurrentOperation=next((operation for operation in operations if operation["operator"]=="XOR" and operation["firstOperand"]==sumTemp), None)
      realDeal=newCurrentOperation["firstOperand"]
    else:
      realDeal=newCurrentOperation["secondOperand"]

    newCurrentOperation=next((operation for operation in operations if operation["targetRegister"]==realDeal), None)
    newCurrentOperation["targetRegister"]=temp
    newCurrentOperation=next((operation for operation in operations if operation["targetRegister"]==temp), None)
    newCurrentOperation["targetRegister"]=realDeal

    risArray.append(temp)
    risArray.append(realDeal)
    return realDeal
  else:
    # print("non posso farcela")
    return None

def findCorrectZ(temp, currentOperation, currentIdx, operations, risArray):
  z="z"+padNumberString(currentIdx)

  newCurrentOperation=next((operation for operation in operations if operation["targetRegister"]==z), None)

  currentOperation["targetRegister"]=z
  newCurrentOperation["targetRegister"]=temp
  risArray.append(z)
  risArray.append(temp)
  # print("tuttoapposto")
  return z

def findTheRealOtherAnswer(sumTemp, currentCarrier, operations,risArray):
  newCurrentOperation=next((operation for operation in operations if operation["operator"]=="XOR" and operation["firstOperand"]==currentCarrier ), None)
  if newCurrentOperation==None:
    newCurrentOperation=next((operation for operation in operations if operation["operator"]=="XOR" and operation["secondOperand"]==currentCarrier ), None)
    realSumTemp=newCurrentOperation["firstOperand"]
  else:
    realSumTemp=newCurrentOperation["secondOperand"]

  # print("sumTemp quello vero", realSumTemp)
  oldCurrentOperation=next((operation for operation in operations if operation["targetRegister"]==sumTemp), None)
  newCurrentOperation=next((operation for operation in operations if operation["targetRegister"]==realSumTemp), None)
  oldCurrentOperation["tagetRegister"]=realSumTemp
  newCurrentOperation["targetRegister"]=sumTemp
  
  risArray.append(sumTemp)
  risArray.append(realSumTemp)
  return realSumTemp, sumTemp


def continueAnswer(currentIndex, currentCarrier, operations, carriersArray, risArray):
  # A binary sum use the following 5 operations to complete a digit:
  # 1 A xoR B = sumTemp
  # 2 A and B = CoutTemp
  # 3 Cout(-1) xor sumTemp = Z
  # 4 Cout(-1) and sumTemp = CoutYemp
  # 5 CoutTemp or CoutYemp = Cout(0) -> it will be next cout(-1)
  # Technically A, B and Cout(-1) can be swapped intercycle but the input use these in this order, so it's ok

  currentOperation=next((operation for operation in operations if operation["operator"]=="XOR" and operation["firstOperand"]=="x"+padNumberString(currentIndex)), None)
  sumTemp=currentOperation["targetRegister"]
  if sumTemp[0]=="z":
    # print("Error Detected 1", currentOperation)
    return
  
  currentOperation=next((operation for operation in operations if operation["operator"]=="AND" and operation["firstOperand"]=="x"+padNumberString(currentIndex)), None)
  coutTemp=currentOperation["targetRegister"]
  if coutTemp[0]=="z":
    # print("Error Detected 2", currentOperation)
    coutTemp=fixThingsWithZ(coutTemp, operations, sumTemp, currentOperation, carriersArray, currentIndex, risArray)
    # print("Error Solved")

  currentOperation=next((operation for operation in operations if operation["operator"]=="XOR" and operation["firstOperand"]==currentCarrier and operation["secondOperand"]==sumTemp), None)
  if currentOperation==None:
    currentOperation=next((operation for operation in operations if operation["operator"]=="XOR" and operation["secondOperand"]==currentCarrier and operation["firstOperand"]==sumTemp), None)
    if currentOperation==None:
      # print("Error Detected 3 Not Found", sumTemp, "XOR", currentCarrier, currentOperation)
      sumTemp, oldSumTemp=findTheRealOtherAnswer(sumTemp, currentCarrier, operations, risArray)
      if coutTemp==sumTemp:
        coutTemp=oldSumTemp
      currentOperation=next((operation for operation in operations if operation["operator"]=="XOR" and (operation["firstOperand"]==currentCarrier or operation["secondOperand"]==currentCarrier)), None)
      # print("Error solved")
  z=currentOperation["targetRegister"]
  if z!="z"+padNumberString(currentIndex):
    # print("Error Detected 3 Wrong Answer", currentOperation)
    z=findCorrectZ(z, currentOperation, currentIndex, operations, risArray)
    # print("Error Solved")

  currentOperation=next((operation for operation in operations if operation["operator"]=="AND" and operation["firstOperand"]==currentCarrier and operation["secondOperand"]==sumTemp), None)
  if currentOperation==None:
    currentOperation=next((operation for operation in operations if operation["operator"]=="AND" and operation["secondOperand"]==currentCarrier and operation["firstOperand"]==sumTemp), None)
    if currentOperation==None:
      # print("Error Detected 4 Not Found", currentOperation)
      return 
  coutYemp=currentOperation["targetRegister"]
  if coutYemp[0]=="z":
    # print("Error Detected 4 Wrong Answer", currentOperation)
    return
  
  
  currentOperation=next((operation for operation in operations if operation["operator"]=="OR" and operation["firstOperand"]==coutTemp and operation["secondOperand"]==coutYemp), None)
  if currentOperation==None:
    currentOperation=next((operation for operation in operations if operation["operator"]=="OR" and operation["secondOperand"]==coutTemp and operation["firstOperand"]==coutYemp), None)
    if currentOperation==None:
      # print("Error Detected 5 Not Found", coutTemp, "OR", coutYemp, currentOperation)
      return 
  currentCarrier=currentOperation["targetRegister"]
  if currentCarrier[0]=="z":
    # print("Error Detected 5 Wrong Answer", currentOperation)
    currentCarrier=fixThingsWithZ(currentCarrier, operations, sumTemp,  currentOperation, carriersArray, currentIndex, risArray)
    # print("Error solved")
    return

  return currentCarrier

def solveB():
  rows=getOldAocInput(24)
  registers, operations=parseRows(rows)
  current=0
  currentCarrier=startAnswer(current, operations)
  carriersArray=[]
  carriersArray.append(currentCarrier)
  risArray=[]
  current=current+1

  lenArrayOfKeys=len([k for k in registers.keys() if k[0]=="x"])-1

  while(len(operations)>0 and current<lenArrayOfKeys):
    currentCarrier=continueAnswer(current, currentCarrier, operations, carriersArray, risArray)
    carriersArray.append(currentCarrier)
    current=current+1
  
  risArray.sort()
  return ",".join(risArray)

print(solve())
print(solveB())

# def timeElapse():
#   print(solve())
#   print(solveB())

# print(evaluateTime(timeElapse))