from utility import *

def buildContainerBag(rows):
  containerBags={}

  for row in rows:
    rowSplitted=row.split(" bags contain ")
    contained=rowSplitted[1].split(", ")
    for element in contained:
      elementSplitted=element.split(" ")
      theElement=elementSplitted[1]+" "+elementSplitted[2]
      if(containerBags.get(theElement)==None):
        containerBags[theElement]=[]
      containerBags[theElement].append(rowSplitted[0])
  return containerBags

def buildStandardBag(rows):
  standardBags={}

  for row in rows:
    rowSplitted=row.split(" bags contain ")
    contained=rowSplitted[1].split(", ")
    standardBags[rowSplitted[0]]=[]
    for element in contained:
      elementSplitted=element.split(" ")
      if(elementSplitted[0]=="no"):
        continue
      standardBags[rowSplitted[0]].append({"quantity":int(elementSplitted[0]), "bag": elementSplitted[1]+" "+elementSplitted[2]})
  return standardBags

def solveB():
  rows= getOldAocInput(7)
  standardBags=buildStandardBag(rows)
  realBorder={"shiny gold":1}
  badBorder=set()
  badBorder.add("shiny gold")
  count=-1
  while(len(badBorder)>0):
    nameBag=badBorder.pop()
    qBag=realBorder.pop(nameBag)
    count=count+qBag
    for element in standardBags[nameBag]:
      badBorder.add(element["bag"])
      realBorder[element["bag"]]=qBag*element["quantity"]+realBorder.get(element["bag"],0)
  
  return count

def solveA():
  rows= getOldAocInput(7)
  containerBags=buildContainerBag(rows)
  border=["shiny gold"]
  marked=set()
  while(len(border)>0):
    bag=border.pop()
    marked.add(bag)
    for element in containerBags.get(bag, []):
      if(element not in marked):
        border.append(element)
  return len(marked)-1


print(solveA())
print(solveB())
