from utility import *
from intCode import *

def solve():
  rows=getOldAocInput(7)
  commands=parseIntCode(rows)
  elements={"0":1, "1":1, "2":1, "3":1, "4":1,}
  permutations=[]
  homeMadePermutations(elements, "", 5, permutations)
  possibleResults=[]
  for permutation in permutations:
    currentOutput=0
    for i in range(5):
      permutationCommands=commands.copy()
      inputs=[int(permutation[i]), currentOutput]
      _, outputs, _, _=runCommands(permutationCommands, inputs)
      currentOutput=outputs[-1]
    possibleResults.append(outputs[-1])
  return max(possibleResults)

def solveB():
  rows=getOldAocInput(7)
  commands=parseIntCode(rows)
  elements={"5":1, "6":1, "7":1, "8":1, "9":1,}
  permutations=[]
  homeMadePermutations(elements, "", 5, permutations)
  possibleResults=[]
  for permutation in permutations:
    currentOutput=0
    permutationCommands=[commands.copy() for _ in range(5)]
    permutationCursor=[0 for _ in range(5)]
    for i in range(5):
      inputs=[int(permutation[i]), currentOutput]
      permutationCommands[i], outputs, permutationCursor[i], finish=runCommands(permutationCommands[i], inputs, permutationCursor[i], True)
      currentOutput=outputs[-1]
    while(finish==False):
      for i in range(5):
        inputs=[currentOutput]
        permutationCommands[i], outputs, permutationCursor[i], finish=runCommands(permutationCommands[i], inputs, permutationCursor[i], True)
        if finish==False or len(outputs)>0:
          currentOutput=outputs[-1]
    possibleResults.append(currentOutput)
  return max(possibleResults)


  # runCommands(commands, inputs)
  # return commands

print(solve())
print(solveB())

# def timeElapse():
#   print(solve("a"))
#   print(solve("b"))

# print(evaluateTime(timeElapse))
