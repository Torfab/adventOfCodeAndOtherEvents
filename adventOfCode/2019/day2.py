from utility import *
from intCode import *

def parseRows(rows):
  return [int(x) for x in rows[0].split(",")]

def solve(part):
  rows=getOldAocInput(2)
  commands=parseRows(rows)
  if part=="a":
    commands[1]=12
    commands[2]=2
    runCommands(commands)
    return commands[0]
  if part=="b":
    for noun in range(100):
      for verb in range(100):
        newCommands=commands.copy()
        newCommands[1]=noun
        newCommands[2]=verb
        result=runCommands(newCommands)
        if result[0]==19690720:
          return 100*noun+verb
    return "non ho trovato niente"
print(solve("a"))
print(solve("b"))

# def timeElapse():
#   print(solve())
#   print(solveB())

# print(evaluateTime(timeElapse))
