from utility import *

def parseRows(rows):
  return [int(x) for x in rows]

def parseRows3(rows):
  start=rows[0]
  end=rows[-1]
  mul=1
  for element in rows[1:-1]:
    first, second=element.split('|')
    mul=mul*int(second)//int(first)
  return int(start), int(end), mul


def solve():
  rows=openFile("raw.txt")
  gears=parseRows(rows)
  movements=gears[0]*2025
  
  return movements//gears[-1]

def solve2():
  rows=openFile("raw.txt")
  gears=parseRows(rows)
  movements=10000000000000*gears[-1]

  return - (movements// -gears[0])

def solve3():
  rows=openFile("raw.txt")
  start, end, multiplier=parseRows3(rows)
  movements=start*100*multiplier

  return movements//end

# print(solve())
# print(solve2())
print(solve3())
