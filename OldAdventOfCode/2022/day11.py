from utility import *


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
        monkeys[monkeyIdx]["items"].append(dict(value=int(item)))
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

def playARound(monkeys, part, modulo):
  for monkey in monkeys:
    for itemIdx in range(len(monkey["items"])):
      newValue=doOperation(monkey["items"][0]["value"], monkey["operation"])
      newValue=newValue%modulo
      if(part=="a"):
        newValue=newValue//3

      if(newValue%monkey["test"]==0):
        monkeys[monkey["throwIfTrue"]]["items"].append(dict(value=newValue))
      else:
        monkeys[monkey["throwIfFalse"]]["items"].append(dict(value=newValue))

      monkey["inspected"]=monkey["inspected"]+1
      monkey["items"].pop(0)

def solve(days, part):
  rows= getOldAocInput(11)
  monkeys=comprehension(rows)
  
  modulo=1
  for monkey in monkeys:
    modulo=modulo*monkey["test"]

  for i in range(days):
    playARound(monkeys, part, modulo)

  resultArray=[]
  for monkey in monkeys:
    resultArray.append(monkey["inspected"])
  resultArray.sort()
  result=resultArray[-1]*resultArray[-2]
  
  return result

print(solve(20,"a"))
print(solve(10000,"b"))
submitToday(solve(10000, "b"))