from utility import *

def buildElementInOrbitalDict(root, deep, passiveConnectionDict):
  newPlanet={}
  newPlanet["name"]=root
  newPlanet["deepness"]=deep
  newPlanet["arrayOfOrbital"]=[buildElementInOrbitalDict(x, deep+1, passiveConnectionDict) for x in passiveConnectionDict.get(root, [])]
  return newPlanet

def parseRows(rows):
  passiveConnectionDict={}
  setOfReceiver=set()
  setOfSenders=set()
  for row in rows:
    rowSplitted=row.split(")")
    if len(rowSplitted)==1:
      rowSplitted=row.split("(")
      firstElement=rowSplitted[1]
      secondElement=rowSplitted[0]
    else:
      firstElement=rowSplitted[0]
      secondElement=rowSplitted[1]
    setOfReceiver.add(firstElement)
    setOfSenders.add(secondElement)
    passiveConnectionDict[firstElement]=passiveConnectionDict.get(firstElement, [])+[secondElement]
  
  root=list(setOfReceiver.difference(setOfSenders))[0]
  #Name, deepness, connection
  orbitalDict=buildElementInOrbitalDict(root, 0, passiveConnectionDict)
  return orbitalDict

def findOrbitals(orbitalDictionary):
  ris=orbitalDictionary["deepness"]
  for element in orbitalDictionary["arrayOfOrbital"]:
    ris=ris+findOrbitals(element)
  return ris

def findElementInTree(orbitalDictionary, element, path):
  if (orbitalDictionary["name"]==element):
    return orbitalDictionary, path
  else:
    for orb in orbitalDictionary["arrayOfOrbital"]:
      result=findElementInTree(orb, element, {**path, orbitalDictionary["name"]:orbitalDictionary["deepness"]})
      if result:
        return result
  return None

def solve(part):
  rows=getOldAocInput(6)
  orbitalDictionary=parseRows(rows)
  if part=="a":
    return findOrbitals(orbitalDictionary)
  if part=="b":
    startPoint="YOU"
    endPoint="SAN"#TA
    # My plan is to reach (counting steps) the first common ancestor. at worst is COM
    # Sadly i've not a real linked list so i've to start from COM everytime.
    # If i knew that was asked i would've built a different data structure to start with, but it's ok
    # 9ms on my okaish CPU
    startElement, pathStart=findElementInTree(orbitalDictionary, startPoint,{})
    endElement, pathEnd=findElementInTree(orbitalDictionary, endPoint, {})
    pathStartKeys=list(pathStart.keys())
    pathEndKeys=list(pathEnd.keys())
    _, firstAncestor=thingInCommonArrayWithValue(list(reversed(pathStartKeys)), list(reversed(pathEndKeys)))
    return startElement["deepness"]-pathStart[firstAncestor]+endElement["deepness"]-pathEnd[firstAncestor]-2


# print(solve("a"))
# print(solve("b"))


def timeElapse():
  print(solve("a"))
  print(solve("b"))

print(evaluateTime(timeElapse))
