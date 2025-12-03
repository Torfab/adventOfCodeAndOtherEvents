from utilityz import *

def parseRows(rows):
  return rows

def findVoltage(row):
  intRow=[int(x) for x in row]
  firstElement=max(intRow)
  idx=intRow.index(firstElement)
  if idx+1<len(intRow):
    secondElement=max(intRow[idx+1:])
    
  else:
    intRow.pop(idx)
    secondElement=firstElement
    firstElement=max(intRow)
  return firstElement*10+secondElement

def findRealVoltage(row, num):
  intRow=[int(x) for x in row]
  result=0
  cursor=0
  num=num-1
  while(num>0):
    maxNum=max(intRow[cursor:-num])
    cursor=cursor+intRow[cursor:-num].index(maxNum)+1
    result=result+maxNum*(10**(num))
    num=num-1
  
  maxNum=max(intRow[cursor:])
  cursor=intRow[cursor:].index(maxNum)
  result=result+maxNum*(10**(num))
  return result
  
def solve(num):
  rows=getOldAocInput(3)
  rows=parseRows(rows)
  sumz=0
  for row in rows:
    sumz=sumz+findRealVoltage(row, num)  
  return sumz

print(solve(2))
print(solve(12))
