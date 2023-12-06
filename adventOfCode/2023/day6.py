from utility import *
import re
import math

def timesWin(time, distance):
  # x(a-x)>b => -x2+ax-b>0 => x2-ax+b<0   a=1, b=-time, c=distance     (time+-sqrt(time2-4distance))/2
  start = math.ceil((time-(time**2-4*distance)**(1/2))/2)
  end = math.floor((time+(time**2-4*distance)**(1/2))/2)

  return end-start+1


def solve(part):
  rows=getOldAocInput(6)
  if(part=="a"):
    times=[int(x) for x in re.split("\s+", rows[0])[1:]]
    distances=[int(x) for x in re.split("\s+", rows[1])[1:]]
  if(part=="b"):
    times=[int(rows[0].split(":")[1].replace(" ", ""))]
    distances=[int(rows[1].split(":")[1].replace(" ", ""))]
  result=1
  for i in range(len(times)):
    result=result*timesWin(times[i], distances[i])
  return result

print(solve("a"))
print(solve("b"))