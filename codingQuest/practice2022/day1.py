from utility import *

rows=openFile("input.txt")

def move(position1, movement, grid):
  if(movement==0):
    return position1
  else:
    position1=position1+movement
    if (position1 > len(grid)-1):
      # return move(len(grid)-1, len(grid)-1-position1, grid)
      position=len(grid)-1
      return position
    # print("sono alla posizione", position1, "mi muovo di ", grid[position1], "lol")
    return move(position1, grid[position1], grid)
  

def solve(rowsSize: int):
  grid=[]
  position1=0
  position2=0
  for idx, row in enumerate(rows):
    if(idx<rowsSize):
      splitted=row.split(" ")
      if(idx%2!=0):
        splitted.reverse()
      grid.extend(splitted)
      continue
    if(idx==rowsSize):
      grid.reverse()
      grid=[int(x) for x in grid]
      # print(len(grid))
    movement1,movement2=[int(x) for x in row.split(" ")]
    # print("t", idx-rowsSize+1, "p1")
    position1=move(position1, movement1, grid)
    # print("posizione finale", position1)
    # print("t", idx-rowsSize+1, "p2")
    position2=move(position2, movement2, grid)
    # print("posizione finale", position2)
    if (position1==len(grid)-1):
      # print("1", idx-rowsSize+1)
      return 1*(idx-rowsSize+1)
    if (position2==len(grid)-1):
      # print("2", idx-rowsSize+1)
      return 2*(idx-rowsSize+1)
print(solve(20))
# print(solve(6))