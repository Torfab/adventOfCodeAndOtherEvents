import requests
import math
from utility import *

def buildGrid():
  grid=[]
  for _ in range(100):
    tempRow=[]
    for _ in range(100):
      tempRow.append(".")
    grid.append(tempRow)
  return grid

def printGrid(grid):
  for row in range(len(grid)):
    for column in range(len(grid[0])):
      print(grid[row][column], end="")
    print()

def putAsteroidInGrid(asteroid, grid):
  column, row, horizontal, vertical=[int(x) for x in asteroid.split(" ")]
  for element in range(3600, 3660):
    currentColumn= math.floor(column + horizontal*element)
    currentRow= math.floor(row+vertical*element)
    if(0<=currentColumn<100 and 0<=currentRow<100):
      grid[currentRow][currentColumn]="#"

def findSafeSpot(grid):
  for idxRow in range(len(grid)):
    for idxColumn in range(len(grid[0])):
      if(grid[idxRow][idxColumn]=="."):
        return idxColumn, idxRow

def solve():
  response = requests.get("https://codingquest.io/api/puzzledata?puzzle=23")
  rows = response.text.splitlines()
  grid=buildGrid()
  # printGrid(grid)
  for row in rows:
    putAsteroidInGrid(row, grid)
    # print(row)
  # printGrid(grid)
  
  x,y=findSafeSpot(grid)

  return str(x)+":"+str(y)

print(solve())