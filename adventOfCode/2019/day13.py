from utility import *
from intCode import *

# Technically i need to a lot less information, considering the program will update itself, 
# But having complete information helps in debug
def updateGrid(grid, output):
  cursor=0
  while(cursor<len(output)):
    toDraw=output[cursor+2]
    if(toDraw==0):
      toDraw="."
    elif(toDraw==1):
      toDraw=blockChar
    elif(toDraw==2):
      toDraw="#"
    elif(toDraw==3):
      toDraw="-"
    elif(toDraw==4):
      toDraw="O"
    else:
      toDraw="H"
    grid[(output[cursor], output[cursor+1])]=toDraw
    cursor=cursor+3
  return grid

# Orders of frame is always Paddle, Points, Balls
# So i check if i need paddle movement
# Then i check if i do points, and multiple points
# Then i check WHERE i need to move the ball
# Program ends when it reach op 99, so i can just track that one
def stampaFrame(grid, commands, cursor, relativeBase, paddlePositionX, ballPositionX):
  realOutput=[]
  if paddlePositionX==ballPositionX:
    paddleMovement=0
  elif paddlePositionX>ballPositionX:
    paddleMovement=-1
  else:
    paddleMovement=1
  if paddleMovement!=0:
    for _ in range(6):
      _, output, cursor, _, relativeBase=runCommands(commands, paddleMovement, pauseMode=True, cursor=cursor, relativeBase=relativeBase)
      realOutput=realOutput+output
    paddlePositionX=realOutput[3]
    updateGrid(grid, realOutput)
    realOutput=[]
  #Check point or ball movement
  for _ in range(6):
    _, output, cursor, _, relativeBase=runCommands(commands, paddleMovement, pauseMode=True, cursor=cursor, relativeBase=relativeBase)
    realOutput=realOutput+output
  while(realOutput[3]==-1):
    points=realOutput[5]
    updateGrid(grid, realOutput)
    realOutput=[]
    for _ in range(6):
      _, output, cursor, finish, relativeBase=runCommands(commands, paddleMovement, pauseMode=True, cursor=cursor, relativeBase=relativeBase)
      realOutput=realOutput+output
    if(finish):
      return cursor, relativeBase, paddlePositionX, ballPositionX, points

  updateGrid(grid, realOutput)
  ballPositionX=realOutput[3]

  return cursor, relativeBase, paddlePositionX, ballPositionX, -1
  
def solve(part):
  rows=getOldAocInput(13)
  commands=parseIntCode(rows)
  _, output, cursor, _, relativeBase=runCommands(commands)
  grid={}
  updateGrid(grid, output)
  if(part=="a"):
    return len([k for k,v in grid.items() if v=="#"])
  if part=="b":
    commands[0]=2
    realOutput=[]
    cursor=0
    relativeBase=0
    # This is the screen (empyrical, we couldn't know before)
    for _ in range(2508):
      _, output, cursor, _, relativeBase=runCommands(commands, pauseMode=True, cursor=cursor, relativeBase=relativeBase)
      realOutput=realOutput+output
    updateGrid(grid, realOutput)
    paddlePositionX=[k for k,v in grid.items() if v=="-"][0]
    ballPositionX=[k for k,v in grid.items() if v=="O"][0]
    realOutput=[]
    #First of all it put the scoreboard, it is out of our plan so i put it outside of main loop
    for _ in range(3):
      _, output, cursor, _, relativeBase=runCommands(commands, pauseMode=True, cursor=cursor, relativeBase=relativeBase)
      realOutput=realOutput+output
    realOutput=[]

    # Orders of action is always Board, Points, Ball
    # So i can do a frame of the game
    # The main loop just check if there is final result

    points=-1
    while(points==-1):
      cursor, relativeBase, paddlePositionX, ballPositionX, points=stampaFrame(grid, commands, cursor, relativeBase, paddlePositionX, ballPositionX)
    return points

print(solve("a"))
print(solve("b"))