from utility import *

operations={
  "+": lambda x,y: x+y,
  "*": lambda x,y: x*y
}

def plainSolveRow(row):
  rowSplitted=row.split(" ")
  firstOperand=int(rowSplitted[0])
  cursor=0
  lenRowSplitted=len(rowSplitted)
  while(cursor+2<lenRowSplitted):
    operator=rowSplitted[cursor+1]
    secondOperand=int(rowSplitted[cursor+2])
    firstOperand=operations[operator](firstOperand, secondOperand)
    cursor=cursor+2
  return str(firstOperand)

def weirdPrecedenceSolveRow(row):
  rowSplitted=row.split(" ")
  while("+" in rowSplitted):
    idx=rowSplitted.index("+")
    firstOperand=int(rowSplitted[idx-1])
    secondOperand=int(rowSplitted[idx+1])
    rowSplitted[idx-1]=str(firstOperand+secondOperand)
    rowSplitted.pop(idx)
    rowSplitted.pop(idx)

  firstOperand=int(rowSplitted[0])
  cursor=0
  lenRowSplitted=len(rowSplitted)
  while(cursor+2<lenRowSplitted):
    secondOperand=int(rowSplitted[cursor+2])
    firstOperand=firstOperand * secondOperand
    cursor=cursor+2
  return str(firstOperand)

def evaluateRow(row, precedenceFunction):
  lastIdxStart=row.find("(")
  while(lastIdxStart!=-1):
    newIdxStart=row.find("(", lastIdxStart+1)
    while(newIdxStart!=-1):
      lastIdxStart=newIdxStart
      newIdxStart=row.find("(", newIdxStart+1)
    idxEnd=row.find(")", lastIdxStart+1)
    row=row.replace(row[lastIdxStart:idxEnd+1], precedenceFunction(row[lastIdxStart+1:idxEnd]))
    lastIdxStart=row.find("(")
  return int(precedenceFunction(row))

def solve(part):
  rows=getOldAocInput(18)
  if part=="a":
    precedenceFunction=plainSolveRow
  if part=="b":
    precedenceFunction=weirdPrecedenceSolveRow
  ris=0
  for row in rows:
    ris=ris+evaluateRow(row, precedenceFunction)
  return ris


print(solve("a"))
print(solve("b"))

# def timeElapse():
#   print(solve("a"))
#   print(solve("b"))

# print(evaluateTime(timeElapse))

