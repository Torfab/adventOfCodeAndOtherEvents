from utility import *

def solve(days):
  rows= getAocInput(6,2021)

  lanternFishs=[0]*9

  for element in rows[0].split(','):
    lanternFishs[int(element)]=lanternFishs[int(element)]+1

  for day in range(days):
    for idx, element in enumerate(lanternFishs):
      if(idx==0):
        newFish=element
        continue
      lanternFishs[idx-1]=lanternFishs[idx]
    lanternFishs[6]=lanternFishs[6]+newFish
    lanternFishs[8]=newFish
      
  return sum(lanternFishs)

print(solve(80))
print(solve(256))