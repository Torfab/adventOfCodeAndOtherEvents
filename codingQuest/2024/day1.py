from utility import *

itemsToAdd=["Seat", "Meals", "Luggage", "Fee", "Tax"]
itemsToRemove=["Discount", "Rebate"]

def parseRows(rows):
  collectionOfItems={}
  for row in rows:
    key, value=row.split(": ")
    name, number=value.split(" ")
    if (collectionOfItems.get(key)==None):
      collectionOfItems[key]=0
    if name in itemsToAdd:
      toAdd=1
    elif name in itemsToRemove:
      toAdd=-1
    collectionOfItems[key]=collectionOfItems[key]+toAdd*int(number)
  return collectionOfItems


def solve():
  rows=openFile("input.txt")
  collectionOfItems=parseRows(rows)
  print(collectionOfItems)
  return min(collectionOfItems.values())
print(solve())