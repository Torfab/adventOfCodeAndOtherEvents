from utilityz import *

directions=fromDistanceBuildSetOfDirections(1)

def parseRows(rows):
  runicWords=rows[0].split(":")[1].split(",")
  text=rows[2].split(" ")
  return runicWords, text

def parseRows2(rows):
  words=rows[0].split(":")[1].split(",")
  
  newArr=[]
  for element in range(2, len(rows)):
    newArr.append(rows[element])

  banana=(words,newArr)

  return banana


def solve():
  rows=openFile("raw.txt")
  runicWords, text=parseRows(rows)
  count=0
  for element in runicWords:
    for word in text:
      if element in word:
        count=count+1
  return count

def updateGrid(index, length, grid):
  for element in range(index, index+length):
    grid[element]= True

def solve2():
  rows=openFile("raw.txt")
  myTuple=parseRows2(rows)
  count=0
  word=""
  for word in myTuple[1]:
    truthyGrid={x:False for x in range(len(word))}
    for runic in myTuple[0]:
      idxRune=word.find(runic)
      while(idxRune!=-1):
        updateGrid(idxRune, len(runic), truthyGrid)
        idxRune=word.find(runic,idxRune+1)
      
      idxRune=word[::-1].find(runic)
      while(idxRune!=-1):
        updateGrid(len(word)-idxRune-len(runic), len(runic), truthyGrid)
        idxRune=word[::-1].find(runic,idxRune+1)
    count=count+sum(truthyGrid.values())

  return(count)

def parseRows3(rows):
  words=rows[0].split(":")[1].split(",")
  
  grid={}
  truthyGrid={}
  for y in range(2, len(rows)):
    for x in range(0, len(rows[2])):
      grid[(x,y-2)]=rows[y][x]
      truthyGrid[(x,y-2)]=False

  return words, grid, truthyGrid


def solve3():
  rows=openFile("raw.txt")
  runic, grid, truthyGrid=parseRows3(rows)
  maxX, maxY=maxGrid(grid)
  for rune in runic:
    charIdx=0
    x=0
    y=0
    maxLen=len(rune)
    while(y<maxY+1):
      while(x<maxX+1):
        if(rune[0]==grid[(x,y)]):
          tentativeList=[(x,y)]
          charIdx=1
          for direction in directions:
            toCheck=(x,y)
            completed=True
            while(charIdx<maxLen):
              toCheck=(toCheck[0]+direction[0])%(maxX+1), (toCheck[1]+direction[1])
              if(grid.get(toCheck)==rune[charIdx]):
                tentativeList.append(toCheck)
                charIdx=charIdx+1
              else:
                completed=False
                break
            if completed:
              for element in tentativeList:
                truthyGrid[element]=True
            tentativeList=[(x,y)]
            charIdx=1
        x=x+1
      x=0
      y=y+1
  return sum(truthyGrid.values())

print(solve())
print(solve2())
print(solve3())
