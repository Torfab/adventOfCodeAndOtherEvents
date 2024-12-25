from utility import *

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

#DEPRECATED, but i keep it here for legacy
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

#DEPRECATED, but i keep it here for legacy
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
    # print("It shouldn't happen")
    return None

#DEPRECATED, but i keep it here for legacy
def findCorrectZ(temp, currentOperation, currentIdx, operations, risArray):
  z="z"+padNumberString(currentIdx)

  newCurrentOperation=next((operation for operation in operations if operation["targetRegister"]==z), None)

  currentOperation["targetRegister"]=z
  newCurrentOperation["targetRegister"]=temp
  risArray.append(z)
  risArray.append(temp)
  # print("tuttoapposto")
  return z

#DEPRECATED, but i keep it here for legacy
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

#DEPRECATED, but i keep it here for legacy
def continueAnswer(currentIndex, currentCarrier, operations, carriersArray, risArray):
  # A binary sum use the following 5 operations to complete a digit:
  # 1 A xoR B = sumTemp
  # 2 A and B = carrierTemp
  # 3 lastCarrier xor sumTemp = Z
  # 4 lastCarrier and sumTemp = carrierYemp
  # 5 carrierTemp or carrierYemp = currentCarriage (considering it's last operation i save it directly as last carriage of next iteration)
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

#DEPRECATED, but i keep it here for legacy
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

# New approach, we do not have to swap and fix the sum, therefore we can just improve our detection mechanism and that's it.
# Probably it will be less comprehensive, but surely is less tailored on my input. I think it's comprehensive enough tho.
# First thing i checked, there is no overwrite register and there are no redherring operations. 
# All the operations make sense and are not redundant so we can use the occurances of them to find result
def solveC():
  rows=getOldAocInput(24)
  _, operations=parseRows(rows)

  # Idea behind is still having those operations to do in order, in particular sumTemp appear twice and carrierTemp once
  # 1 A xoR B = sumTemp
  # 2 A and B = carrierTemp
  # 3 lastCarrier xor sumTemp = Z
  # 4 lastCarrier and sumTemp = carrierYemp
  # 5 carrierTemp or carrierYemp = currentCarriage (considering it's last operation i save it directly as last carriage of next iteration)

  #First thing first, we know that left part of operations are good, so i save which register appear twice and which once
  ris=[]
  dictCounter={}
  for operation in operations:
    dictCounter[operation["firstOperand"]]=dictCounter.get(operation["firstOperand"], 0)+1
    dictCounter[operation["secondOperand"]]=dictCounter.get(operation["secondOperand"], 0)+1

  # The only iterations that do not work as explained are the very first one (there is no carriage) 
  # And the very last one (there is no things to sum on carriage)
  # Input looks tailored to not have any problem on those, if you find you have too few elements you can try to check them
  # Anyway we delete from operations the firsts and the lasts, firsts start with x00, and last is with z45 (or last element)
  deleteFirst=[operation for operation in operations if operation["firstOperand"]=="x00"]
  for operation in deleteFirst:
    operations.remove(operation)
  listZ=[operation for operation in operations if operation["targetRegister"][0]=="z"]
  lastElement="z"+padNumberString(len(listZ))
  deleteLast=next(operation for operation in operations if operation["targetRegister"]==lastElement)
  operations.remove(deleteLast)

  #Now we consider the different scenario just looking at what we expect
  #sumTemps should appear twice, carrierTemp once, lastCarrier twice and carrierYemp once.
  #Xor element with x/y register should write NO Z
  #Xor element without x/y register should write Z elements
  sumTemps=[]
  carrierTemp=[]
  lastCarriers=[]
  carrierYemp=[]
  shouldBeZed=[]
  shouldNotBeZed=[]
  for operation in operations:
    if operation["operator"]=="XOR" and operation["firstOperand"][0]=="x":
      sumTemps.append(operation["targetRegister"])
    elif operation["operator"]=="AND" and operation["firstOperand"][0]=="x":
      carrierTemp.append(operation["targetRegister"])
    elif operation["operator"]=="XOR" and operation["firstOperand"][0]!="x":
      shouldBeZed.append(operation["targetRegister"])
    elif operation["operator"]=="AND" and operation["firstOperand"][0]!="x":
      carrierYemp.append(operation["targetRegister"])
    elif operation["operator"]=="OR":
      lastCarriers.append(operation["targetRegister"])
    else:
      shouldNotBeZed.append(operation["targetRegister"])

  #now that i've all the datastructures filled we just do the checks
  for element in shouldBeZed:
    if element[0]!="z":
      ris.append(element)
  for element in shouldNotBeZed:
    if element[0]=="z":
      ris.append(element)
  for element in carrierTemp:
    if dictCounter.get(element)!=1:
      ris.append(element)
  for element in sumTemps:
    if dictCounter.get(element)!=2:
      ris.append(element)
  for element in lastCarriers:
    if dictCounter.get(element)!=2:
      ris.append(element)
  for element in carrierYemp:
    if dictCounter.get(element)!=1:
      ris.append(element)

  #put in order and send answer
  ris.sort()
  return ",".join(ris)

print(solve())
print(solveC())

def timeElapse():
  print(solve())
  print(solveC())

print(evaluateTime(timeElapse))