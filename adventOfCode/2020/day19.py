from utilityz import *

rules={}

def parseRows(rows):
  state="rules"
  rules={}
  messages=[]
  for row in rows:
    if row=="":
      state="messages"
      continue
    if(state=="rules"):
      rowSplitted=row.split(": ")
      keyRule=int(rowSplitted[0])
      values=rowSplitted[1]
      if values[0]=="\"":
        rules[keyRule]=[values[1]]
        continue
      valuesSplitted=values.split("|")
      arrayOfPossibilites=[]
      for value in valuesSplitted:
        arrayOfPossibilites.append([int(x) for x in value.split()])
      rules[keyRule]=arrayOfPossibilites
      continue
    if(state=="messages"):
      messages.append(row)
  return rules, messages

def findOkRules(ruleKey, idx, message):
  if(idx==len(message)):
    return -1
  realIdx=idx
  if ruleKey=="a" or ruleKey=="b":
    if message[idx]==ruleKey:
      if idx==len(message)-1:
        return True
      return idx+1
    else:
      return -1
  possibilities=rules[ruleKey]
  solutions=[]
  for possibility in possibilities:
    atWhichPoint=0
    idx=realIdx
    while(atWhichPoint<len(possibility)):
      idx=findOkRules(possibility[atWhichPoint], idx, message)
      if(idx is True):
        print(atWhichPoint, len(possibility)-1)
        if(atWhichPoint==(len(possibility)-1)):
          return True
        return -1
      if(idx==-1):
        break
      atWhichPoint=atWhichPoint+1
    if idx!=-1:
      solutions.append(idx)
  if len(solutions)>0:
    print(solutions)
    return solutions[0]
  return -1

def checkMessage(message):
  resultIdx=findOkRules(0, 0, message)
  if(resultIdx==True):
    return True
  if(resultIdx==-1):
    return False
  elif resultIdx==len(message):
    return True
  else:
    return False
  


def solve():
  rows=getOldAocInput(19)
  global rules
  rules, messages=parseRows(rows)
  ris=0
  for message in messages:
    if(checkMessage(message)):
      ris=ris+1
  return ris

def updateRules():
  global rules
  rules[8]=[[42],[42,8]]
  rules[11]=[[42, 31], [42,11,31]]
  print(rules)

def solveB():
  rows=getOldAocInput(19)
  global rules
  rules, messages=parseRows(rows)
  updateRules()
  ris=0
  for message in messages:
    if(checkMessage(message)):
      print(message)
      ris=ris+1
  return ris


# print(solve())
print(solveB())

# def timeElapse():
#   print(solve())
#   print(solveB())

# print(evaluateTime(timeElapse))

