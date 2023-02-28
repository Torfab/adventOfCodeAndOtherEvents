from utility import *

rows=openFile("input.txt")

def buildRect1Visualization(rect1):
  rect1List=[]
  for _ in range(rect1["height"]):
    temp=[]
    for _ in range(rect1["width"]):
      temp.append(0)
    rect1List.append(temp)
  return rect1List

def stampaRect(rectMap):
  for row in range(len(rectMap)):
    for column in range(len(rectMap[0])):
      print(rectMap[row][column], end='')
    print()


def intersectionTwoRectangles(rect1, rect2):
  x2start=rect2["x"]-rect1["x"]
  y2start=rect2["y"]-rect1["y"]
  x2end=x2start+rect2["width"]-1
  y2end=y2start+rect2["height"]-1

  xstart=max(0, x2start)
  
  ystart= max(0, y2start)
  xend = min(rect1["width"]-1, x2end)
  yend= min(rect1["height"]-1, y2end)
  if (xstart<=xend and ystart<=yend):
    return [xstart, ystart, xend, yend]


def removeElement(rectMap, elementsToRemove):
  for i in range(elementsToRemove[1],elementsToRemove[3]+1):
    for j in range(elementsToRemove[0], elementsToRemove[2]+1):

      rectMap[i][j]=1



# rect1={'x': 0, 'y': 0, 'width': 20, 'height': 4}
# rect2={'x': -10, 'y': 0, 'width': 20, 'height': 10}

# rect1V=buildRect1Visualization(rect1)

# elementsToRemove=(intersectionTwoRectangles(rect1,rect2))
# print(elementsToRemove)

# removeElement(rect1V, elementsToRemove)
# stampaRect(rect1V)

def countRectangle(rect1V, value):
  accumulatore=0
  for i in rect1V:
    accumulatore=accumulatore+i.count(value)
  return accumulatore

rows=[x.split(" ") for x in rows]
rows=[{'x':int(x[0]), 'y': int(x[1]), 'width': int(x[2]), 'height': int(x[3])} for x in rows]

spaziRiempiti=0
for idx, rect in enumerate(rows):
  rect1V=buildRect1Visualization(rect)
  for element in range(idx+1, len(rows)):
    elementsToRemove=(intersectionTwoRectangles(rect,rows[element]))
    if(elementsToRemove):
      removeElement(rect1V, elementsToRemove)
  spaziRiempiti=spaziRiempiti+countRectangle(rect1V, 0)
  print("cambio rect", spaziRiempiti, idx, rect)
print(spaziRiempiti)
print(20000*100000-spaziRiempiti)