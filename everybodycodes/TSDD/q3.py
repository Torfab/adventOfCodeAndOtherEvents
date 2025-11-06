from utility import *

def parseRows(rows):
  return [int(x) for x in rows[0].split(',')]


def solve():
  rows=openFile("raw.txt")
  crates=parseRows(rows)
  crates=list(set(crates))
  crates.sort()
  return sum(crates)
def solve2():
  rows=openFile("raw.txt")
  crates=parseRows(rows)
  crates=list(set(crates))
  crates.sort()
  # crates.reverse()
  return sum(crates[:20])

def solve3():
  rows=openFile("raw.txt")
  crates=parseRows(rows)
  counterDict={}
  for element in crates:
    counterDict[element]=counterDict.get(element, 0)+1
  return max(counterDict.values())


# print(solve())
# print(solve2())
print(solve3())
