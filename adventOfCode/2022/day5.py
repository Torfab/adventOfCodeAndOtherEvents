from utility import *


def parseRows(rows: list):
  columns=[]
  for number in range(9):
    columns.append([])
  movements=[]
  for element in rows:
    if(element=='' or element[1]=='1'):
      continue
    if(element[0]=="m"):
      movements.append(element)
    else:
      for idx in range(9):
        if(element[1+idx*4]!=' '):
          columns[idx].insert(0,element[1+idx*4])

  return columns, movements

def useCrate9000(columns, quantityToMove, fromColumn, toColumn):
  for element in range(quantityToMove):
    columns[toColumn].append(columns[fromColumn].pop())

def useCrate9001(columns, quantityToMove, fromColumn, toColumn):
  for element in range(quantityToMove):
    columns[toColumn].append(columns[fromColumn].pop(-quantityToMove+element))

def solve(useMachinery):
  
  rows= getOldAocInput(5)

  columns, movements=parseRows(rows)

  for movement in movements:
    splitted=movement.split(" ")
    quantityToMove=int(splitted[1])
    fromColumn=int(splitted[3])-1
    toColumn=int(splitted[5])-1

    useMachinery(columns, quantityToMove, fromColumn, toColumn)
  
  result=''
  for idx in range(len(columns)):
    result+=columns[idx][-1]
    
  return result

print(solve(useCrate9000))
print(solve(useCrate9001))
