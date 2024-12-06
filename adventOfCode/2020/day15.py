from utility import *

def solve(nth):
  rows=getOldAocInput(15)
  turns=[int(x) for x in rows[0].split(",")]
  gameState={}
  currentTurn=1

  for element in turns[:-1]:
    gameState[element]=(currentTurn)
    currentTurn=currentTurn+1

  # My whole solution is based on updating the value AFTER the next loop
  # so i've to exclude last input element from the state, i will use it in first iteration of main
  element=turns[-1]
  currentTurn=currentTurn+1

  while currentTurn<=nth:
    lastElement=element
    element=currentTurn-1-gameState.get(lastElement, currentTurn-1)
    # Little speed improvement cause if it fail the search element have to be
    # It needs constantly 1 access every loop while explicit handling need 2 access in worst case (not found)
    # in the end the speed up is ~7.5%

    gameState[lastElement]=currentTurn-1
    currentTurn=currentTurn+1
  return element

print(solve(2020))
print(solve(30000000))

# Don't really like the speed but i don't think there is anything alghorithmically intensive 
# Just 2 access in O(1), couple of assignments with single unit increments/decrements, only using int numbers
# I can understand that 3million loops are not istant in an interpreted language
# So i guess it's just python spending python time
