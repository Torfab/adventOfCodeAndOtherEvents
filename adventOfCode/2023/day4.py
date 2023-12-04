from utility import *

# def solve(part):
#   rows=getOldAocInput(4)
#   result=0
#   for row in rows:
#     row=row.split(":")
#     numbers=row[1].split("|")
#     winningNumbers=numbers[0].strip().split(" ")
#     realWinningNumbers=[]
#     for element in winningNumbers:
#       if (element==""):
#         continue
#       else:
#         realWinningNumbers.append(element)
#     potentialNumbers=numbers[1].strip().split(" ")
#     realPotentialNumbers=[]
#     for element in potentialNumbers:
#       if (element==""):
#         continue
#       else:
#         realPotentialNumbers.append(element)
#     partialResult=0
#     for element in realWinningNumbers:
#       if element in realPotentialNumbers:
#         if(partialResult==0):
#           partialResult=1
#         else:
#           partialResult=partialResult*2
#     result=result+partialResult
#   return result

def solve(part):
  rows=getOldAocInput(4)
  result=0
  instances={}
  card=1
  for element in rows:
    instances[card]=1
    card=card+1
  for row in rows:
    row=row.split(":")

    numbers=row[1].split("|")
    winningNumbers=numbers[0].strip().split(" ")
    realWinningNumbers=[]
    for element in winningNumbers:
      if (element==""):
        continue
      else:
        realWinningNumbers.append(element)
    potentialNumbers=numbers[1].strip().split(" ")
    realPotentialNumbers=[]
    for element in potentialNumbers:
      if (element==""):
        continue
      else:
        realPotentialNumbers.append(element)
    game=row[0].split(" ")
    realRow=[]
    for element in game:
      if (element==""):
        continue
      else:
        realRow.append(element)
    game=int(realRow[1])
    partialResult=0
    for element in realWinningNumbers:
      if element in realPotentialNumbers:
        partialResult=partialResult+1
    for element in range(partialResult):
      instances[game+element+1]=instances[game+element+1]+instances[game]
  result=sum(instances.values())


  return result

submitToday(solve("a"))
# print(solve("b"))