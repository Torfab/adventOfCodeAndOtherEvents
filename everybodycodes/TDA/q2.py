from utilityz import *

def parseRows(rows):
  gridLocation={}
  commands=[]
  for row in rows:
    rowSplitted=row.split("=")
    if rowSplitted[0]!="MOVES":
      gridLocation[rowSplitted[0]]=tuple([int(x) for x in rowSplitted[1][1:-1].split(",")])
    else:
      commands=rowSplitted[1]
  return  gridLocation, commands

def solve(part):
  rows=openFile("raw.txt")
  gridLocation, commands=parseRows(rows)
  illuminated=set()
  illuminated.add(gridLocation["START"])
  cursor=gridLocation["START"]
  if part!=3:
    for element in commands:
      toGo=sumTupleValueByValue(cursor, gridLocation[element])
      toGo=(toGo[0]//2, toGo[1]//2)
      illuminated.add(toGo)
      cursor=toGo
  else:
    border=set()
    border.add(cursor)
    commandsList=["A","B","C"]
    newBorder=border
    while(len(border)>0):
      newBorder=set()
      for element in border:
        for command in commandsList:
          toGo=sumTupleValueByValue(element, gridLocation[command])
          toGo=(toGo[0]//2, toGo[1]//2)
          if(toGo not in illuminated):
            illuminated.add(toGo)
            newBorder.add(toGo)
      border=newBorder

  if(part==1):
    return len(illuminated)

  fireFlies=set()
  directions=fromDistanceBuildSetOfDirections(1)
  for element in illuminated:
    for direction in directions:
      tentative=sumTupleValueByValue(element, direction)
      if(tentative not in illuminated):
        fireFlies.add(tentative)
  return len(fireFlies)

print(solve(3))