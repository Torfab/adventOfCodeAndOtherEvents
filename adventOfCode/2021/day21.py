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
    if(values[player]>=1000):
      break
    player=(player+1)%2
  result=min(values)*diceRolls*3

  return result


def buildQuantumDices():
  quantumDices={}
  for d1 in range(1,4):
    for d2 in range(1,4):
      for d3 in range(1,4):
        dTot=d1+d2+d3
        if(quantumDices.get(dTot)==None):
          quantumDices[dTot]=1
        else:
          quantumDices[dTot]=quantumDices[dTot]+1
  return quantumDices

def solveB():
  rows=getOldAocInput(21)
  positions=parseRows(rows)
  wins=[0,0]

  quantumDices=buildQuantumDices()
  states={(positions[0], positions[1], 0, 0): 1}
  turn=1
  while(len(states)>0):
    newStates={}
    turn=(turn+1)%2
    notTurn=(turn+1)%2
    
    for k, v in states.items():
      for d,q in quantumDices.items():
        newTuple=[0,1,2,3]
        newTuple[turn]=(k[turn]+d)%10
        newTuple[notTurn]=k[notTurn]
        scoreTurn=k[turn+2]+newTuple[turn]+1
        if(scoreTurn>=21):
          wins[turn]=wins[turn]+q*v
          continue
        newTuple[turn+2]=scoreTurn
        newTuple[notTurn+2]=k[notTurn+2]
        newTuple=tuple(newTuple)
        if(newStates.get(newTuple)==None):
          newStates[newTuple]=q*v
        else:
          newStates[newTuple]=newStates[newTuple]+q*v
    states=newStates
  return max(wins)

print(solve())
print(solveB())