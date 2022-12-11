from utility import *


def solve(slidingSpace):
  rows=getAocInput(1,2021)
  rowsButInt=[int(a) for a in rows]
  larger=0
  for idx in range(len(rowsButInt)-slidingSpace):
    if (rowsButInt[idx]<rowsButInt[idx+slidingSpace]):
      larger=larger+1

  return larger

print(solve(1))
print(solve(3))