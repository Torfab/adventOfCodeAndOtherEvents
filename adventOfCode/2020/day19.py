from utility import *

# One of harder days for me, i didn't want to use a regex and i didn't know how to really handle the problem
# After several ideas, i went to the idea of path finding between result space.
# Solution is slow but is generic, it has no problem handling any kind of formal language with this kind of rules.

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

#DEPRECATED it's here only for legacy, this solves part 1 but i used another strategy for part 1/2
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
        if(atWhichPoint==(len(possibility)-1)):
          return True
        return -1
      if(idx==-1):
        break
      atWhichPoint=atWhichPoint+1
    if idx!=-1:
      solutions.append(idx)
  if len(solutions)>0:
    return solutions[0]
  return -1

#DEPRECATED it's here only for legacy, this solves part 1 but i used another strategy for part 1/2
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
  

def checkMessageB(message):
  idxToCheck=0
  startPath=rules[0][0]
  border=[([(startPath, 0)], idxToCheck, "F")]
  lenMessage=len(message)
  while(len(border)>0):
    fullPath, idxToCheck, direction=border.pop()
    if len(fullPath)==0:
      if(idxToCheck==lenMessage):
        return True
      else:
        continue
    if idxToCheck==lenMessage and direction=="F":
      continue
    lastElementOfPath, choice=fullPath[-1]
    if(isinstance(lastElementOfPath, str)):
      if lastElementOfPath==message[idxToCheck]:
        border.append((fullPath[:len(fullPath)-1], idxToCheck+1, "B"))
      continue
    if direction=="F":
      for element in rules[lastElementOfPath[choice]]:
        border.append((fullPath+[(element,0)], idxToCheck, "F"))
      continue
    if direction=="B":
      if(choice<len(lastElementOfPath)-1):
        fullPath[-1]=(fullPath[-1][0], choice+1)
        for element in rules[lastElementOfPath[choice+1]]:
          border.append((fullPath+[(element,0)], idxToCheck, "F"))
      else:
        border.append((fullPath[:len(fullPath)-1], idxToCheck, "B"))
  return False

# DEPRECATED it's here only for legacy, this solves part 1 but i used another strategy for part 1/2
# It's a bit faster tho
def solveDEPRECATED():
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

def solve(part):
  rows=getOldAocInput(19)
  global rules
  rules, messages=parseRows(rows)
  if part=="b":
    updateRules()
  ris=0
  for message in messages:
    if(checkMessageB(message)):
      ris=ris+1
  return ris

print(solve("a"))
print(solve("b"))

# def timeElapse():
#   print(solve("a"))
#   print(solve("b"))

# print(evaluateTime(timeElapse))

