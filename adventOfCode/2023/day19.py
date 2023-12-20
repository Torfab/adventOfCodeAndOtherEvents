from utility import *

def parseRows(rows):
  rules={}
  commands=[]
  mode=0
  for row in rows:
    if(row==""):
      mode=1
      continue
    if(mode==0):
      rowSplitted=row.split("{")
      key=rowSplitted[0]
      subRules=rowSplitted[1].split(",")
      ruleList=[]
      for idx in range(len(subRules)):
        ruleList.append(subRules[idx])
      for idx in range(len(ruleList)-1):
        newSplit=ruleList[idx].split(":")
        ruleList[idx]={"result":newSplit[1], "unit": newSplit[0][0], "operation": newSplit[0][1], "number": int(newSplit[0][2:])}
      ruleList[-1]={"always":ruleList[-1][:-1]}
      rules[key]=ruleList

    if(mode==1):
      rowSplitted=row[1:len(row)-1].split(",")
      newDict={}
      for split in rowSplitted:
        key=split[0]
        number=int(split[2:])
        newDict[key]=number
      commands.append(newDict)


  return rules, commands

def checkValue(label, rules, command):
  if(label=="A"):
    return True
  if(label=="R"):
    return False
  for singleRule in rules[label]:
    if(singleRule.get("always")!=None):
      return checkValue(singleRule["always"], rules, command)
    if(singleRule["operation"]==">" and command[singleRule["unit"]] > singleRule["number"]):
      return checkValue(singleRule["result"], rules, command)
    if(singleRule["operation"]=="<" and command[singleRule["unit"]] < singleRule["number"]):
      return checkValue(singleRule["result"], rules, command)

  return False

def findValue(key, rules, rangeX, rangeM, rangeA, rangeS, arrayA):
  if(key=="R"):
    return
  if(key=="A"):
    arrayA.append((rangeX[1]-rangeX[0]+1)*(rangeM[1]-rangeM[0]+1)*(rangeA[1]-rangeA[0]+1)*(rangeS[1]-rangeS[0]+1))
    return
  rangeRimanenteX=list(rangeX)
  rangeRimanenteM=list(rangeM)
  rangeRimanenteA=list(rangeA)
  rangeRimanenteS=list(rangeS)
  for singleRule in rules[key]:
    if(singleRule.get("always")!=None):
      findValue(singleRule["always"], rules, tuple(rangeRimanenteX), tuple(rangeRimanenteM), tuple(rangeRimanenteA), tuple(rangeRimanenteS), arrayA)
      continue

    if(singleRule["unit"]=="x" and rangeRimanenteX[0]<=rangeRimanenteX[1]):

      if(singleRule["operation"]==">"  and rangeRimanenteX[1]>singleRule["number"]):
        findValue(singleRule["result"], rules, (max(rangeRimanenteX[0], singleRule["number"]+1), rangeRimanenteX[1]), tuple(rangeRimanenteM), tuple(rangeRimanenteA), tuple(rangeRimanenteS), arrayA)
        rangeRimanenteX[1]=min(rangeRimanenteX[1], singleRule["number"])

      if(singleRule["operation"]=="<" and rangeRimanenteX[0]<singleRule["number"]):
        findValue(singleRule["result"], rules, (rangeRimanenteX[0],min(rangeRimanenteX[1], singleRule["number"]-1)), tuple(rangeRimanenteM), tuple(rangeRimanenteA), tuple(rangeRimanenteS), arrayA)
        rangeRimanenteX[0]=max(rangeRimanenteX[0], singleRule["number"])
      continue


    if(singleRule["unit"]=="m" and rangeRimanenteM[0]<=rangeRimanenteM[1]):

      if(singleRule["operation"]==">"  and rangeRimanenteM[1]>singleRule["number"]):
        findValue(singleRule["result"], rules, tuple(rangeRimanenteX) , (max(rangeRimanenteM[0], singleRule["number"]+1), rangeRimanenteM[1]), tuple(rangeRimanenteA), tuple(rangeRimanenteS), arrayA)
        rangeRimanenteM[1]=min(rangeRimanenteM[1], singleRule["number"])

      if(singleRule["operation"]=="<" and rangeRimanenteM[0]<singleRule["number"]):
        findValue(singleRule["result"], rules, tuple(rangeRimanenteX) , (rangeRimanenteM[0],min(rangeRimanenteM[1], singleRule["number"]-1)), tuple(rangeRimanenteA), tuple(rangeRimanenteS), arrayA)
        rangeRimanenteM[0]=max(rangeRimanenteM[0], singleRule["number"])
      continue


    if(singleRule["unit"]=="a" and rangeRimanenteA[0]<=rangeRimanenteA[1]):

      if(singleRule["operation"]==">"  and rangeRimanenteA[1]>singleRule["number"]):
        findValue(singleRule["result"], rules, tuple(rangeRimanenteX), tuple(rangeRimanenteM), (max(rangeRimanenteA[0], singleRule["number"]+1), rangeRimanenteA[1]), tuple(rangeRimanenteS), arrayA)
        rangeRimanenteA[1]=min(rangeRimanenteA[1], singleRule["number"])

      if(singleRule["operation"]=="<" and rangeRimanenteA[0]<singleRule["number"]):
        findValue(singleRule["result"], rules, tuple(rangeRimanenteX), tuple(rangeRimanenteM), (rangeRimanenteA[0],min(rangeRimanenteA[1], singleRule["number"]-1)), tuple(rangeRimanenteS), arrayA)
        rangeRimanenteA[0]=max(rangeRimanenteA[0], singleRule["number"])
      continue

    if(singleRule["unit"]=="s" and rangeRimanenteS[0]<=rangeRimanenteS[1]):

      if(singleRule["operation"]==">"  and rangeRimanenteS[1]>singleRule["number"]):
        findValue(singleRule["result"], rules, tuple(rangeRimanenteX), tuple(rangeRimanenteM), tuple(rangeRimanenteA), (max(rangeRimanenteS[0], singleRule["number"]+1), rangeRimanenteS[1]), arrayA)
        rangeRimanenteS[1]=min(rangeRimanenteS[1], singleRule["number"])

      if(singleRule["operation"]=="<" and rangeRimanenteS[0]<singleRule["number"]):
        findValue(singleRule["result"], rules, tuple(rangeRimanenteX), tuple(rangeRimanenteM), tuple(rangeRimanenteA), (rangeRimanenteS[0],min(rangeRimanenteS[1], singleRule["number"]-1)), arrayA)
        rangeRimanenteS[0]=max(rangeRimanenteS[0], singleRule["number"])

  return sum(arrayA)



def solve(part):
  rows=getOldAocInput(19)
  rules, commands=parseRows(rows)
  if(part=="a"):
    accepted=0
    for command in commands:
      if(checkValue("in", rules, command)):
        for value in command.values():
          accepted=accepted+value
    return accepted
  if(part=="b"):
    return findValue("in", rules, (1,4000),(1,4000),(1,4000),(1,4000), [])
  
print(solve("a"))
print(solve("b"))