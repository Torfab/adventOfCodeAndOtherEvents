from utilities import *


def comprehension(rows):

  rows=[row.strip() for row in rows]

  monkeys=[]
  monkeyIdx=0
  for idx, element in enumerate(rows):
    if(idx%7==0):
      splitted= element.split(" ")
      monkeyIdx=int(splitted[1][0])
      monkeys.append(dict())
      monkeys[monkeyIdx]["inspected"]=0
    if(idx%7==1):
      splitted= element.split(" ")
      items=[int(item.rstrip(",")) for item in splitted[2:]]
      monkeys[monkeyIdx]["items"]= []
      for item in items:
        monkeys[monkeyIdx]["items"].append(dict(value=int(item), monkeyHolders=[monkeyIdx]))
    if(idx%7==2):
      splitted= element.split(" ")
      operation=splitted[3:]
      monkeys[monkeyIdx]["operation"]= operation
    if(idx%7==3):
      splitted= element.split(" ")
      test=splitted[-1]
      monkeys[monkeyIdx]["test"]= int(test)
    if(idx%7==4):
      splitted= element.split(" ")
      throwIfTrue=splitted[-1]
      monkeys[monkeyIdx]["throwIfTrue"]= int(throwIfTrue)
    if(idx%7==5):
      splitted= element.split(" ")
      throwIfFalse=splitted[-1]
      monkeys[monkeyIdx]["throwIfFalse"]= int(throwIfFalse)
  return monkeys

def doOperation(value, operation):
  if (operation[0]=="old"):
    firstAddendum=value
  else:
    firstAddendum = int(operation[0])
  if (operation[2]=="old"):
    secondAddendum=value
  else:
    secondAddendum = int(operation[2])

  if(operation[1]=='+'):
    return firstAddendum + secondAddendum
  if(operation[1]=='*'):
    return firstAddendum * secondAddendum

  return "absurd"

def playARound(monkeys, part):
  for monkey in monkeys:
    for itemIdx in range(len(monkey["items"])):
      newValue=doOperation(monkey["items"][0]["value"], monkey["operation"])
      if(part=="a"):
        newValue=newValue//3
      if(newValue%monkey["test"]==0):
        monkey["items"][0]["monkeyHolders"].append(monkey["throwIfTrue"])
        monkeys[monkey["throwIfTrue"]]["items"].append(dict(value=newValue, monkeyHolders=monkey["items"][0]["monkeyHolders"]))
      else:
        monkey["items"][0]["monkeyHolders"].append(monkey["throwIfFalse"])
        monkeys[monkey["throwIfFalse"]]["items"].append(dict(value=newValue, monkeyHolders=monkey["items"][0]["monkeyHolders"]))
      monkey["items"].pop(0)

def equalsArraybyValue(a,b):
  if(len(a)!=len(b)):
    return False
  for idx in range(len(a)):
    if(a[idx]!=b[idx]):
      return False
  return True

def findRepetition(myArray):
  newArray=myArray.copy()
  index=0
  if (len(newArray)%2==1):
    index=index+1
    newArray.pop(0)
  while(len(newArray)>0):
    if(equalsArraybyValue(newArray[(len(newArray)//2):], newArray[:(len(newArray)//2)])):
      #print("ho trovato parte ricorsiva", newArray[len(newArray)//2:])
      return index, newArray[len(newArray)//2:]
    else:
      newArray.pop(0)
      newArray.pop(0)
      index=index+2
  return 0,[]

print(findRepetition([1,0,0,0,0,0]))

def solve(days, part):
  rows= getAocInput(-1)

  monkeys=comprehension(rows)
  itemsQuantity=0
  for monkey in monkeys:
    itemsQuantity=itemsQuantity+len(monkey["items"])

  for i in range(days):
    playARound(monkeys, part)
    if((i+1)%51==0):
      print("ahahah")
      for monkey in monkeys:
        for itemIdx in reversed(range(len(monkey["items"]))):
          repetitionIndex, periodicPart=findRepetition(monkey["items"][itemIdx]["monkeyHolders"])
          if(len(periodicPart)!=0):

            for index in range(repetitionIndex):
              monkeys[monkey["items"][itemIdx]["monkeyHolders"][index]]["inspected"]=monkeys[monkey["items"][itemIdx]["monkeyHolders"][index]]["inspected"]+1

            # repetitionBeforeEnd=days//len(periodicPart)
            # for element in periodicPart:
            #   monkeys[element]["inspected"]=monkeys[element]["inspected"]+repetitionBeforeEnd

            # resto=days%len(periodicPart)
            # for index in range(resto):
            #   monkeys[periodicPart[index]]["inspected"]=monkeys[periodicPart[index]]["inspected"]+1

            monkey["items"].pop(itemIdx)
            itemsQuantity=itemsQuantity-1

  for monkey in monkeys:
    for item in monkey["items"]:
      for elementIdx in range(len(item["monkeyHolders"])-1):
        monkeys[item["monkeyHolders"][elementIdx]]["inspected"]=monkeys[item["monkeyHolders"][elementIdx]]["inspected"]+1

    monkey["items"]=[]

  resultArray=[]
  for monkey in monkeys:
    resultArray.append(monkey["inspected"])

  return resultArray

  # resultArray.sort()
  # result=resultArray[-1]*resultArray[-2]
  return

print(solve(1,"b"))
print(solve(20,"b"))
print(solve(1000,"b"))
# print(solve(2000,"b"))
# print(solve(3000,"b"))
# print(solve(4000,"b"))
# print(solve(5000,"b"))
# print(solve(6000,"b"))
# print(solve(7000,"b"))
# print(solve(8000,"b"))
# print(solve(9000,"b"))
# print(solve(10000,"b"))
print(solve(10000,"b"))