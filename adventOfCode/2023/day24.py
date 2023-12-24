from utility import *

X=0
Y=1
Z=2
VX=3
VY=4
VZ=5

M=0
Q=1

def parseRows(rows):
  hailstones=[]
  for row in rows:
    row=row.replace(" @", ",")
    row=[int(x) for x in row.split(", ")]
    hailstones.append(row)
  return hailstones

def constraintLine(hail):
  m=hail[VY]/hail[VX]
  q=hail[Y]-m*hail[X]

  return (m,q)

def buildHailLines(hails):
  hailLines=[]
  for element in hails:
    hailLines.append(constraintLine(element))
  return hailLines

def intersect(line1, line2):
  if(line1[M]==line2[M]):
    return None

  x=(line1[Q]-line2[Q])/ (line2[M]-line1[M])

  y=x*line1[M]+line1[Q]

  return (x,y)

def checkInside(leftLimit, rightLimit, intersection,a,b):
  # print(intersection)
  if(intersection==None):
    return False
  if(intersection[0]>=leftLimit and intersection[0]<=rightLimit):
    if(intersection[1]>=leftLimit and intersection[1]<=rightLimit):
        # first element is negative if on left, second if direction is left
        # first element is negative if on right, second if direction is on right
        # they have to be discorded to be put inside
      if ((a[X]-intersection[0])*a[VX]) <0:
        if ((b[X]-intersection[0])*b[VX]) <0:
          return 1
  return 0

def solveA():
  rows=getOldAocInput(24)
  hails=parseRows(rows)
  hailsLines=buildHailLines(hails)

  limitLeft=200000000000000
  limitRight=400000000000000

  result=0
  for idx in range(len(hailsLines)-1):
    for jdx in range(idx+1, len(hailsLines)):
      result=result+checkInside(limitLeft, limitRight, intersect(hailsLines[idx], hailsLines[jdx]), hails[idx], hails[jdx])

  return result

def solveB():
  rows=getOldAocInput(24)
  hails=parseRows(rows)
  hailsLines=buildHailLines(hails)


  PotentialXSet=None
  PotentialYSet=None
  PotentialZSet=None
  for idx in range(len(hailsLines)-1):
    for jdx in range(idx+1, len(hailsLines)):
      APx, APy, APz, AVx, AVy, AVz=hails[idx]
      BPx, BPy, BPz, BVx, BVy, BVz=hails[jdx]

      if(AVx == BVx):
        newXSet= set()
        difference=BPx-APx
        for v in range(-1000, 1000):
          if(v==AVx):
            newXSet.add(v)
            continue
          if difference % (v-AVx) == 0:
            newXSet.add(v)
        if(PotentialXSet!=None):
          PotentialXSet=PotentialXSet&newXSet
        else:
          PotentialXSet = newXSet.copy()

      if(AVy == BVy):
        newYSet= set()
        difference=BPy-APy
        for v in range(-1000, 1000):
          if(v==AVy):
            newYSet.add(v)
            continue
          if difference % (v-AVy) == 0:
            newYSet.add(v)
        if(PotentialYSet!=None):
          PotentialYSet=PotentialYSet&newYSet
        else:
          PotentialYSet = newYSet.copy()

      if(AVz == BVz):
        newZSet= set()
        difference=BPz-APz
        for v in range(-1000, 1000):
          if(v==AVz):
            newZSet.add(v)
            continue
          if difference % (v-AVz) == 0:
            newZSet.add(v)
        if(PotentialZSet!=None):
          PotentialZSet=PotentialZSet&newZSet
        else:
          PotentialZSet = newZSet.copy()

  # print(PotentialXSet, PotentialYSet, PotentialZSet)

  RVx, RVy, RVz=PotentialXSet.pop(), PotentialYSet.pop(), PotentialZSet.pop()

  # print(RVx, RVy, RVz)
  APx, APy, APz, AVx, AVy, AVz=hails[0]
  BPx, BPy, BPz, BVx, BVy, BVz=hails[1]

  # now that i've speed i consider the stone still and the hails relative speed
  AVx=AVx-RVx
  BVx=BVx-RVx
  AVy=AVy-RVy
  BVy=BVy-RVy
  AVz=AVz-RVz

  # solved from equation system 
  # (1) APx+t1*AVx = BPx+t2*BVx  
  # (2) APy+t1*AVy = BPy+t2*BVy
  # found t2 with t1 as parameter, and solved for t1
  t1=(BVy*BPx-BVy*APx+BVx*APy-BVx*BPy)//(AVx*BVy-AVy*BVx)
  xpos=APx+t1*AVx
  ypos=APy+t1*AVy
  zpos=APz+t1*AVz

  return xpos+ypos+zpos

print(solveA())
print(solveB())