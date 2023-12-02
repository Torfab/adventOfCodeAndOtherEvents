from utility import *

def parseRows(rows):
  return [int(rows[0][28:])-1, int(rows[1][28:])-1]

def step(position, dice):
  moves=3+dice%100+(dice+1)%100+(dice+2)%100
  position=(position+moves)%10
  return position

def solve():
  rows=getOldAocInput(21)
  positions=parseRows(rows)
  values=[0,0]
  
  currentDice=0
  diceRolls=0
  player=0
  while(True):
    diceRolls=diceRolls+1
    positions[player]=step(positions[player], currentDice)
    currentDice=(currentDice+3)%100
    values[player]=values[player]+positions[player]+1
    # print(diceRolls, currentDice, values)
    # input("step")
    if(values[player]>=1000):
      break
    player=(player+1)%2

  # print(values)
  # print("rolls", diceRolls)

  result=min(values)*diceRolls*3

  return result

print(solve())