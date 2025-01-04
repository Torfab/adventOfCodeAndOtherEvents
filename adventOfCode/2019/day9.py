from utility import *
from intCode import *


def solve(part):
  rows=getOldAocInput(9)
  commands=parseIntCode(rows)
  if part=="a":
    result=runCommands(commands, 1)
  if part=="b":
    result=runCommands(commands, 2)
  output=result[1]
  return output[0]
  # return commands

print(solve("a"))
print(solve("b"))
# print(solve("b"))

# def timeElapse():
#   print(solve("a"))
#   print(solve("b"))

# print(evaluateTime(timeElapse))
