import requests

def buildGrid():
  return [[" " for _ in range(50)] for _ in range(10)]

def stampaGrid(grid):
  for row in range(len(grid)):
    for column in range(len(grid[0])):
      print(grid[row][column], end="")
    print()

def toggleElement(grid, row, column):
  if (grid[row][column]==" "):
    grid[row][column]="█"
  else:
    grid[row][column]=' '

def toggleRectangleInGrid(grid, rectangle):
  column, row, width, height= [int(x) for x in rectangle.split(" ")]

  for idxRow in range(row, row+height):
    for idxColumn in range(column, column+width):
      toggleElement(grid, idxRow, idxColumn)

def solve():
  response = requests.get("https://codingquest.io/api/puzzledata?puzzle=22")
  rows = response.text.splitlines()

  grid=buildGrid()

  for element in rows:
    toggleRectangleInGrid(grid, element)
  
  stampaGrid(grid)

solve()