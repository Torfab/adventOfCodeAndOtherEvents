from utility import *

def parseRows(rows):

  rows=[x.split(" ") for x in rows]

  grid=[]
  for x in range(len(rows[0])):
    newArray=[]
    for y in range(len(rows)):
      newArray.append(int(rows[y][x]))
    grid.append(newArray)
  return grid

def solve1():
  rows=openFile("raw.txt")
  grid=parseRows(rows)
  lenGrid=len(grid)

  for i in range(10):
    idxRowElement=i%lenGrid
    element=grid[idxRowElement].pop(0)
    idxActiveRow=(idxRowElement+1)%lenGrid
    lenRowToTake=len(grid[idxActiveRow])
    if(((element-1)//lenRowToTake+1 )% 2==0):
      # We are coming back
      idxOfInsertion=lenRowToTake-((element%lenRowToTake)-1)  
      if(idxOfInsertion>lenRowToTake):
        idxOfInsertion=idxOfInsertion%lenRowToTake
    else:
      # We are going forward
      idxOfInsertion=(element%lenRowToTake)-1

    grid[idxActiveRow].insert(idxOfInsertion, element)

    shout=""
    for n in grid:
      shout=shout+str(n[0])
  return shout

def solve2():
  rows=openFile("raw.txt")
  grid=parseRows(rows)
  lenGrid=len(grid)
  i=0
  
  shoutCollection={}
  while(True):
    idxRowElement=i%lenGrid
    element=grid[idxRowElement].pop(0)
    idxActiveRow=(idxRowElement+1)%lenGrid
    idxOfInsertion=element-1

    grid[idxActiveRow].insert(idxOfInsertion, element)

    shout=""
    for n in grid:
      shout=shout+str(n[0])
    shout=int(shout)
    shoutCollection[shout]=shoutCollection.get(shout,0)+1
    if(shoutCollection[shout]==2024):
      return (i+1)*shout
    
    i=i+1

def solve3():
  rows=openFile("raw.txt")
  grid=parseRows(rows)
  # print(grid)
  lenGrid=len(grid)
  shoutCollection={}
  arrayOfResults=[]
  for i in range(1000):
    idxRowElement=i%lenGrid
    element=grid[idxRowElement].pop(0)
    idxActiveRow=(idxRowElement+1)%lenGrid
    lenRowToTake=len(grid[idxActiveRow])

    if(((element-1)//lenRowToTake+1 )% 2==0):
      #going right
      idxOfInsertion=lenRowToTake-((element%lenRowToTake)-1)  

      if(idxOfInsertion>lenRowToTake):
        idxOfInsertion=idxOfInsertion%lenRowToTake

    else:
      #going left
      idxOfInsertion=(element%lenRowToTake)-1

    grid[idxActiveRow].insert(idxOfInsertion, element)

    shout=""
    for n in grid:
      shout=shout+str(n[0])
    shout=int(shout)
    arrayOfResults.append(shout)
    shoutCollection[shout]=shoutCollection.get(shout,0)+1

  return max(shoutCollection.keys())

print(solve1())
print(solve2())
print(solve3())


