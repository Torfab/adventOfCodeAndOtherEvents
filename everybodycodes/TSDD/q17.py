import heapq
from utility import *

directions=[(1,0), (0,1), (-1,0), (0,-1)]

def buildGrid(raw):
    grid={}
    start=(-1,-1)
    for y, row in enumerate(raw):
        for x, col in enumerate(row):
            if col=="@":
                col=0
                volcano=(x,y)
            if col=="S":
                col=0
                start=(x,y)
            grid[(x,y)]=int(col)
    return grid, volcano, start


def printGrid(grid):
    maxX=max([x[0] for x in grid.keys()])
    maxY=max([x[1] for x in grid.keys()])
    
    for y in range(maxY+1):
        for x in range(maxX+1):
            print(grid[(x,y)], end="")
        print()
        
def solve():
    raw=openFile("raw.txt")
    grid, volcano, _=buildGrid(raw)
    radius=10
    radiusSquared=radius*radius
    results=[]
    
    for element in grid.keys():
        nearbyness=(volcano[0]-element[0])**2+(volcano[1]-element[1])**2
        if nearbyness<=radiusSquared:
            results.append(element)
    sumz=0
    for element in results:
        sumz=sumz+grid[element]
        
    return sumz
    
def solve2():
    raw=openFile("raw.txt")
    grid, volcano, _=buildGrid(raw)
    maxX=max([x[0] for x in grid.keys()])
    maxRadius=maxX//2
    alreadyBeen=set()
    nearbynessGrid={}
    results=[]
    for k in grid.keys():
        nearbynessGrid[k]=(volcano[0]-k[0])**2+(volcano[1]-k[1])**2
    for radius in range(maxRadius+1):
        destroyed=[]
        radiusSquared=radius*radius
        for k, v in nearbynessGrid.items():
            if k in alreadyBeen:
                continue
            if v<=radiusSquared:
                destroyed.append(k)
        sumz=0
        for element in destroyed:
            sumz=sumz+grid[element]
            alreadyBeen.add(element)
        results.append(sumz)
    print(results)
    return max(results)*results.index(max(results))

def sumTuple(a,b):
    return (a[0]+b[0],a[1]+b[1])    
    
def solve3():
    raw=openFile("raw.txt")
    grid, volcano, start=buildGrid(raw)
    alreadyBeen=set()
    maxX=max([x[0] for x in grid.keys()])
    maxY=max([x[1] for x in grid.keys()])
    halfX=maxX//2
    halfY=maxY//2
    maxRadius=maxX
    nearbynessGrid={}
    for k in grid.keys():
        nearbynessGrid[k]=(volcano[0]-k[0])**2+(volcano[1]-k[1])**2
    for radius in range(maxRadius+1):
        for k,v in nearbynessGrid.items():
            if k in alreadyBeen:
                continue
            if v<=radius*radius:
                nearbynessGrid[k]=radius
                alreadyBeen.add(k)
    
    print("start Dijkstra")

    radius=2
    while(True):
        border=[]        
        alreadyBeen=set()
        heapq.heappush(border, (0, start, (False, False, False, False)))
        for element in [k for k, v in nearbynessGrid.items() if v<=radius]:
            grid.pop(element, None)
        while(border):
            time, position, status=heapq.heappop(border)
            if (position, status) in alreadyBeen:
                continue
            else:
                alreadyBeen.add((position, status))
            if position==start and False not in status:
                print("found")
                if time//30<=radius:
                    print("ALE", time, radius,  time*radius)
                    return time*radius
                else:
                    print("troppo lento", time, "a radius", radius, "provo di meglio")
                    radius=radius+1
                    break
                
            E,S,W,N=status
            for d in directions:
                tentative=sumTupleValueByValue(position, d)
                if grid.get(tentative, None)==None:
                    continue
                else:
                    if tentative[0]==halfX:
                        if tentative[1]<halfY:
                            N=True
                        elif tentative[1]>halfY:
                            S=True
                    elif tentative[1]==halfY:
                        if tentative[0]<halfX:
                            W=True
                        if tentative[0]>halfX:
                            E=True
                heapq.heappush(border, (time+grid[tentative], tentative, (E,S,W,N)))

print("result:", solve3())
