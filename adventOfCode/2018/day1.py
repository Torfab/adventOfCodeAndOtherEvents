from utility import *

def parseRows(rows):
  rows=[int(x) for x in rows]
  return  rows


def solve():
  rows=getOldAocInput(1)
  nums=getOldAocInput(rows)
  result=0
  for num in nums:
    result=result+num
  return result, 

def solve2():
  rows=getOldAocInput(1)
  nums=getOldAocInput(rows)
  resultSet=set()
  result=0
  resultSet.add(result)
  while(True):
    for num in nums:
      result=result+num
      if(result in resultSet):
        return result
      resultSet.add(result)

print(solve())
print(solve2())