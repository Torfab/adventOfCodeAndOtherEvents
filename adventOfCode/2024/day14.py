from utility import *

limits=(100, 102)
# limits=(10,6)

wPart=(0,limits[0]//2-1)
ePart=(limits[0]//2+1, limits[0])
nPart=(0, limits[1]//2-1)
sPart=(limits[1]//2+1, limits[1])

def parseRows(rows):
  robots=[]
  for row in rows:
    rowSplitted=row.split(" ")
    positionRaw=rowSplitted[0].split("=")[1]
    position=tuple(int(x) for x in positionRaw.split(","))
    velocityRaw=rowSplitted[1].split("=")[1]
    velocity=tuple(int(x) for x in velocityRaw.split(","))
    robots.append({"position": position, "velocity":velocity})
  return robots

def checkRobotPosition(robot):
  position=robot["position"]
  if wPart[0]<=position[0]<=wPart[1]:
    if(nPart[0]<=position[1]<=nPart[1]):
      return 0
    elif(sPart[0]<=position[1]<=sPart[1]):
      return 2
    else:
      return 4
  elif (ePart[0]<=position[0]<=ePart[1]):
    if(nPart[0]<=position[1]<=nPart[1]):
      return 1
    elif(sPart[0]<=position[1]<=sPart[1]):
      return 3
    else:
      return 4
  else:
    return 4

def stampaRobot(robots):

  grid={k["position"]: "█" for k in robots}
  stampaGrid(grid)

def solve():
  rows=getOldAocInput(14)
  robots=parseRows(rows)

  for robot  in robots:
    currentPosition=robot["position"]
    velocity=robot["velocity"]
    nextPosition=sumTupleValueByValueWithLoop(currentPosition, ((100*velocity[0]), (100*velocity[1])), limits[0], limits[1])
    robot["position"]=nextPosition

  # print(quadrantNW, quadrantNE, quadrantSW, quadrantSE)

  quadrants=[0,0,0,0,0]
  for robot in robots:
    position=checkRobotPosition(robot)
    quadrants[position]=quadrants[position]+1
  result=1
  for q in quadrants[:-1]:
    result=result*q
  return result

def solveB():
  rows=getOldAocInput(14)
  robots=parseRows(rows)
  # I found by hand that on frame 29 and on frame 80 there is a weird vertical and horizontal pattern
  # Checking first couple of thousands frames those frames would've repeat with same frequency: 103 and 101 times rispectively
  # Having found no reasonable christmas tree yet the idea is to match those vertical and horizontal frames
  # To do that i've to find A and B to solve this equation 30+103A=81+101B with A and B integer
  # Clearly we have an equation with 2 incognites so there will be a family of solution (cycling every 101*103 frames), I've to find the first one
  # To do that i just isolate an incognite (A) and work on the rest A=(51+101B)/103
  # At this point I've to solve for any B that will give me an integer, so using modular arithmetic
  # New equation is 51+101B=0 mod(103) at this point so 101B=-51 (mod 103) so 101B=52 mod(103)
  # At this point i've to divide by 101 but in modular arithmetic is not that simple, so it became B=52 * 101^-1 mod(103)
  # To find modular inverse of 101 mod 3 we use extended euclidean algorithm that find the coefficient of bezout identity
  # Which are the integers x and y such that ax+by=gcd(a,b), the gcd is the only number that can simultaneously satisfy equation and divide the inputs
  # in our case k*101 + m*103=gcd(103,101) and we solve for k=51, m=-50
  # So from B=52*101^-1 mod 103 we have B=52*52 mod 103 that is 77
  # our final formula will be 77*101 (the cycle) + 81 (the starting offset)
  # I know it's not in code but that's what i had to do here

  frame=77*101+81

  for robot  in robots:
    currentPosition=robot["position"]
    velocity=robot["velocity"]
    nextPosition=sumTupleValueByValueWithLoop(currentPosition, ((frame*velocity[0]), (frame*velocity[1])), limits[0], limits[1])
    robot["position"]=nextPosition
  stampaRobot(robots)

  return frame
print(solve())
print(solveB())

# def timeElapse():
#   print(solve())
#   print(solveB())

# print(evaluateTime(timeElapse))

