from utility import *

def toExplode(line):
  countParentheses=0
  flagToExplode=False
  for idx in range(len(line)):
    if line[idx]=="[":
      countParentheses=countParentheses+1
    if line[idx]=="]":
      countParentheses=countParentheses-1

    if countParentheses==5:
      # print("exploding", line)
      flagToExplode=True
      break
  if (not flagToExplode):
    return None
  
  startIdx=idx
  endIdx=idx
  while(True):
    if(line[endIdx]=="]"):
      break
    endIdx=endIdx+1
  
  leftNumber=int(line[startIdx+1:].split(",")[0])
  rightNumber=int(line[startIdx+1:].split(",")[1].split("]")[0])


  leftPart=line[:startIdx]
  rightPart=line[endIdx+1:]

  toChange=None
  trackError=0
  for k in reversed(range(len(leftPart))):
    if(leftPart[k].isnumeric()):
      if(leftPart[k-1].isnumeric()):
        toChange=str(int(leftPart[k-1]+leftPart[k])+leftNumber)
        trackError=-1
      else:
        toChange=str(int(leftPart[k])+leftNumber)
      break
  if(toChange):
    leftPart=leftPart[:k+trackError]+toChange+leftPart[k+1:]

  toChange=None
  
  trackError=1
  for k in range(len(rightPart)):
    if(rightPart[k].isnumeric()):
      if(rightPart[k+1].isnumeric()):
        toChange=str(int(rightPart[k]+rightPart[k+1])+rightNumber)
        trackError=2
      else:
        toChange=str(int(rightPart[k])+rightNumber)
      break
  if(toChange):
    rightPart=rightPart[:k]+toChange+rightPart[k+trackError:]

  newLine=leftPart+"0"+rightPart

  return newLine

def toSplit(line):
  count=0
  flagToSplit=False
  for k in range(len(line)):
    if (line[k].isnumeric()):
      count=count+1
    else:
      count=0
    if (count==2):
      # print("to split", line)
      flagToSplit=True
      break

  if(not flagToSplit):
    return None
  
  num=int(line[k-1:k+1])
  
  if(num%2==0):
    lineToAdd="["+str(num//2)+","+str(num//2)+"]"
  else:
    lineToAdd="["+str(num//2)+","+str((num+1)//2)+"]"
  
  return line[:k-1]+lineToAdd+line[k+1:]


def toAdd(line1, line2):
  line="["+line1+","+line2+"]"

  flagExplodeOk=False
  flagSplitOk=False
  while(not flagExplodeOk or not flagSplitOk):
    flagExplodeOk=False
    flagSplitOk=False

    temp="1"
    while(temp!=None):
      temp=toExplode(line)
      if(temp==None):
        flagExplodeOk=True
        break
      line=temp
    
    temp=toSplit(line)
    if(temp==None):
      flagSplitOk=True
    else:
      line=temp

  return line



def magnitudo(line):
  if(line[0]=="["):
    line=line[1:len(line)-1]
    countP=0
    # print(line[0], line[len(line)-1], line)
    for i in range(len(line)):
      if(line[i]=="["):
        countP=countP+1
      if(line[i]=="]"):
        countP=countP-1
      if(countP==0):
        splitIndex=i+1
        break
    left=line[:splitIndex]
    right=line[splitIndex+1:]
    return magnitudo(left)*3+magnitudo(right)*2
  else:
    element=int(line)
  return element

def solveA():
  rows=getOldAocInput(18)

  result=rows[0]

  for element in rows[1:]:
    result=toAdd(result, element)
    # print(result)


  return magnitudo(result)

# def solveB():

def solveB():
  rows=getOldAocInput(18)
  maximum=0
  for k in range(len(rows)):
    firstAddend=rows[k]
    for z in range(len(rows)):
      if(k==z):
        continue
      secondAddend=rows[z]

      candidateResult=magnitudo(toAdd(firstAddend, secondAddend))
      maximum=max(candidateResult, maximum)
  return maximum

print(solveA()) 
print(solveB()) 