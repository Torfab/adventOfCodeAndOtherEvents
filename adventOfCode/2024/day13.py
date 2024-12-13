from utility import *

def parseRows(rows):
  arrayOfGames=[]
  newButton={}
  for row in rows:
    if(row==""):
      newButton={}
      continue
    splittedRow=row.split(",")
    if(row[0]=="B"):
      x=int(splittedRow[0].split("+")[1])
      y=int(splittedRow[1].split("+")[1])
      newButton[row[7]]=(x,y)
    if(row[0]=="P"):
      targetX=int(splittedRow[0].split("=")[1])
      targetY=int(splittedRow[1].split("=")[1])
      newButton["target"]=(targetX, targetY)
      arrayOfGames.append(newButton)
  return arrayOfGames

def evaluate(element):
  #Ammetto che me la sono andata a riguardare la regola di Cramer
  determinante=element["A"][0]*element["B"][1]-element["A"][1]*element["B"][0]
  detX=element["target"][0]*element["B"][1]-element["target"][1]*element["B"][0]
  detY=element["A"][0]*element["target"][1]-element["A"][1]*element["target"][0]

  Apresses=detX/determinante
  Bpresses=detY/determinante
  if(Apresses.is_integer() and Bpresses.is_integer()):
    return int(3*Apresses), int(Bpresses)
  else:
    return 0,0

def solve(part):
  rows=getOldAocInput(13)
  arrayOfGames=parseRows(rows)

  if(part=="b"):
    for element in arrayOfGames:
      element["target"]=(element["target"][0]+10000000000000, element["target"][1]+10000000000000)
  pushA=0
  pushB=0
  for element in arrayOfGames:
    ris=evaluate(element)
    pushA=pushA+ris[0]
    pushB=pushB+ris[1]

  return pushA+pushB

print(solve("a"))
print(solve("b"))
