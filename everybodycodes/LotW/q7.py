from utility import *
import copy


def parseRows(rows):
  elements= {}
  for row in rows:
    rowSplitted=row.split(", ")
    id=int(rowSplitted[0].split("=")[1])
    energy=int(rowSplitted[1].split("=")[1])
    connections=[int(x) for x in rowSplitted[2].split("=")[1].split(",")]
    elements[id]={"energy": energy, "connections":connections, "impulse":0}
  return elements

def solveForId(id, strength, elements, explosionDeadline):

  border={}
  border[id]={strength:1}
  step=0
  while(border):
    step=step+1
    newBorder={}
    for starter, dictImpulses in border.items():
      for strength, howMany in dictImpulses.items():
        if strength==0 or elements.get(starter)==None:
          continue
        elements[starter]["impulse"]=elements[starter]["impulse"]+strength*howMany
        for connection in elements[starter]["connections"]:
          if(elements.get(connection)==None):
            continue
          newBorder[connection]=newBorder.get(connection, {strength-1:0})
          newBorder[connection][strength-1]=newBorder[connection].get(strength-1,0)+howMany
    border=newBorder

    toExplode=[]
    for idx, element in elements.items():
      element["energy"]=element["energy"]+element.get("impulse",0)
      element["impulse"]=0
      if element["energy"]>explosionDeadline:
        toExplode.append(idx)
        # print(idx, element["energy"])

    for explosion in toExplode:
      if(elements.get(explosion)):
        for connection in elements[explosion]["connections"]:
          if(elements.get(connection)==None):
            continue
          border[connection]=newBorder.get(connection, {10:0})
          border[connection][10]=border[connection].get(10,0)+1
        elements.pop(explosion)

    # print("Stage", step)
    # print(border)
    # for idx,element in elements.items():
    #   print(idx, element["energy"])
    # print()

  result=0
  for element in elements.values():
    result=result+element["energy"]
  return result

def solve(part, firstImpulse, explosionDeadline=1000000):
  rows=openFile("raw.txt")
  elements=parseRows(rows)
  maxConnections=0
  if(part!=3):
    for idx, element in elements.items():
      if len(element["connections"])>maxConnections:
        maxConnections=len(element["connections"])
        mostConnectionsElement=idx
    return solveForId(mostConnectionsElement, firstImpulse, elements, float('inf'))

  maxResult=0
  for idx in elements.keys():
    maxResult=max(maxResult, solveForId(idx, firstImpulse, copy.deepcopy(elements), explosionDeadline))

  return maxResult

# print(solve(3, 10, 1000000))
print(solve(2, 10))
