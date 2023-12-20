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

def solve(part):

  rows=getOldAocInput(19)
  rules, commands=parseRows(rows)
  accepted=0


  for command in commands:
    if(checkValue("in", rules, command)):
      for value in command.values():
        accepted=accepted+value
  return accepted

print(solve("a"))