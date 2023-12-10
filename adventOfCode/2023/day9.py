from utility import *

def elaborateRow(row, part):
  theRows=[]
  if(part=="a"):
    rowSplitted=[int(x) for x in row.split(" ")]
  if(part=="b"):
    rowSplitted=[int(x) for x in row.split(" ")]
    rowSplitted.reverse()
  theRows.append(rowSplitted)
  count=0
  while(True):
    newRow=[]
    for idx in range(len(theRows[count])-1):
      newRow.append(theRows[count][idx+1]-theRows[count][idx])
    theRows.append(newRow)
    count=count+1
    if (all(value == 0 for value in newRow)):
      break
  valueToInsert=0
  for idx in reversed(range(len(theRows))):
    valueToInsert=theRows[idx][-1]+valueToInsert
    theRows[idx].append(valueToInsert)
  return valueToInsert


def solve(part):
  rows=getOldAocInput(9)
  result=0
  for row in rows:
    result=result+elaborateRow(row, part)
  return result

print(solve("a"))
print(solve("b"))