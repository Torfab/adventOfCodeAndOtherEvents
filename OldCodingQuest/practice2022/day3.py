from utility import *
import math

def buildGrid(rows):
  grid=[]
  for row in rows:
    tempRow=[]
    for column in row.split(" "):
      tempRow.append({"value": int(column), "marked": False})
    grid.append(tempRow)
  return grid

def stampaGrid(grid):
  for rows in grid:
    for column in rows:
      print(column["value"], end="")
    print()

def markAsteroidWithValue(grid, row, column):
  borders=set()
  borders.add((row, column))
  value=0
  while(len(borders)!=0):
    newBorders=set()
    for element in borders:
      grid[element[0]][element[1]]["marked"]=True
      value+=grid[element[0]][element[1]]["value"]

      if(element[0]>0 and grid[element[0]-1][element[1]]["marked"]==False and grid[element[0]-1][element[1]]["value"]!=0):
        newBorders.add((element[0]-1, element[1]))

      if(element[0]<len(grid)-1 and grid[element[0]+1][element[1]]["marked"]==False and grid[element[0]+1][element[1]]["value"]!=0):
        newBorders.add((element[0]+1, element[1]))

      if(element[1]<len(grid[0])-1 and grid[element[0]][element[1]+1]["marked"]==False and grid[element[0]][element[1]+1]["value"]!=0):
        newBorders.add((element[0], element[1]+1))

      if(element[1]>0 and grid[element[0]][element[1]-1]["marked"]==False and grid[element[0]][element[1]-1]["value"]!=0):
        newBorders.add((element[0], element[1]-1))
    borders=newBorders
  return value


def solve():

  rows=openFile("input.txt")
  grid=buildGrid(rows)
  
  # stampaGrid(grid)

  numAsteroids=0
  valueAsteroids=0

  for idxRow, row in enumerate(grid):
    for idxColumn, column in enumerate(row):
      if(column["marked"]==True):
        continue
      if(column["value"]!=0):
        newAsteroidValue=markAsteroidWithValue(grid, idxRow, idxColumn)
        valueAsteroids=valueAsteroids+newAsteroidValue
        numAsteroids=numAsteroids+1
        # print(numAsteroids, " trovato nuovo asteroide grande ", newAsteroidValue)

  return math.floor(valueAsteroids/numAsteroids)


print(solve())