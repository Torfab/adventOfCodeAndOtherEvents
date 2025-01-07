from utility import *
import math

def parseRows(rows):
  book={}
  for row in rows:
    rowSplitted=row.split(" => ")
    finishedProduct=rowSplitted[1].split()
    components=rowSplitted[0].split(", ")
    bookComponents={}
    for component in components:
      component=component.split(" ")
      bookComponents[component[1]]=int(component[0])
    book[finishedProduct[1]]={"quantity": int(finishedProduct[0]), "components":bookComponents}
  return book

# There could be a problem of not finding optimal solution if a component is used a lot
# and last item you check has to produce too many filling the saving bucket.
# So it TECHNICALLY could depend by order of components to build, I haven't got this issue so i didn't handle that case
# But if it doesn't work on your input i would've start from this.
def findComponents(target, quantity, book, savedItems):
  if(savedItems.get(target)!=None):
    if(savedItems[target]<quantity):
      quantity=quantity-savedItems[target]
      savedItems.pop(target)
    else:
      savedItems[target]=savedItems[target]-quantity
      if(savedItems[target]==0):
        savedItems.pop(target)
      return 0

  item=book[target]
  times=math.ceil(quantity/book[target]["quantity"])
  savedItems[target]=times*book[target]["quantity"]-quantity
  if(savedItems[target]==0):
    savedItems.pop(target)
  ores=0
  for element, value in item["components"].items():
    if(element=="ORE"):
      ores=ores+times*value
    else:
      ores=ores+findComponents(element, times*value, book, savedItems)

  return ores

def solve(part):
  rows=getOldAocInput(14)
  book=parseRows(rows)

  savedItems={}
  if part=="a":
    return findComponents("FUEL", 1, book, savedItems)
  if part=="b":
    #The idea is that code is fast enough to handle big numbers, so i do a binomial search

    #first Things find boundaries
    end=1
    ores=0
    while(1000000000000-ores>0):
      start=end
      end=end*2
      ores=findComponents("FUEL", end, book, {})

    #Second thing to do is the binomial, so i find middlePoint until the difference is one
    while(end-start>1):
      middlePoint=(start+end)//2
      ores=findComponents("FUEL", (start+end)//2, book, {})
      if 1000000000000-ores>0:
        start=middlePoint
      else:
        end=middlePoint
    return start

print(solve("a"))
print(solve("b"))
