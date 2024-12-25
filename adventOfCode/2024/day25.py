from utilityz import *

def parseRows(rows):
  lenRows=len(rows)
  i=0
  locks=[]
  keys=[]
  while(i<lenRows):
    grid,_,_=buildGrid(rows[i:i+7])
    columns=[]
    for x in range(5):
      columns.append(len([k for k in grid if k[0]==x]))
    if(grid.get((0,0))!=None):
      locks.append(columns)
    else:
      keys.append(columns)
    i=i+8
  return keys, locks

def checkKeyLock(key,lock):
  for x in range(5):
    if(key[x]+lock[x]>7):
      return False
  return True

def solve():
  rows=getOldAocInput(25)
  keys, locks= parseRows(rows)
  ris=0
  for key in keys:
    for lock in locks:
      if(checkKeyLock(key, lock)):
        ris=ris+1
      
  return ris

print(solve())
# print(solveB())

# def timeElapse():
#   print(solve())
#   print(solveB())

# print(evaluateTime(timeElapse))

