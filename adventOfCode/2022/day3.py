from utility import *


def rucksackValue(character):
  if(ord(character)<91):
    return ord(character)-38
  else:
    return ord(character)-96

def solve1():
  rows= getOldAocInput(3)

  spareElements=[]

  i=0

  for rucksack in rows:

    halfSize=int(len(rucksack)/2)
    #print(halfSize)
    firstCompartment=rucksack[0:halfSize]
    secondCompartment=rucksack[halfSize:]

    #print(firstCompartment)
    #print(secondCompartment)

    itemsDictionary= {}

    for item in firstCompartment:
      itemsDictionary[item]=True

    #print(itemsDictionary)

    for item in secondCompartment:
      if(item in itemsDictionary.keys()):
        #print(i, "trovato", item)
        spareElements.append(item)
        break
    i=i+1

  accumulatore=0
  for element in spareElements:
    accumulatore=accumulatore+rucksackValue(element)

  return(accumulatore)

def solve2():
  rows= getOldAocInput(3)
  
  badgeElements=[]

  i=0

  for rucksack in rows:

    if(i%3==0):
      groupElfDictionary={}

    singleElfDictionary= {}
    for item in rucksack:
      singleElfDictionary[item]=True
      
    for item in singleElfDictionary:
      if(item in groupElfDictionary.keys()):
        groupElfDictionary[item]=groupElfDictionary[item]+1
      else:
        groupElfDictionary[item]=1
    
    if(i%3==2):
      badgeElements.append([key for key, value in groupElfDictionary.items() if value==3][0])
    i=i+1
  accumulatore=0
  for element in badgeElements:
    accumulatore=accumulatore+rucksackValue(element)

  
  return accumulatore

print(solve1())
print(solve2())