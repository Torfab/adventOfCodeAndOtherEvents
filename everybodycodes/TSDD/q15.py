import heapq

raw=""
direction=[(1,0),(0,1),(-1,0),(0,-1)]
lenDirection=len(direction)

def sumTuple(a,b):
    return (a[0]+b[0], a[1]+b[1])
    
def mulTuple(tup, k):
    return(tup[0]*k, tup[1]*k)

def solve():
    start=(0,0)
    orders=raw.split(',')
    cursor=1
    grid={}
    current=start
    
    
    for element in orders:
        if element[0]=="R":
            cursor=(cursor-1)%lenDirection
        else:
            cursor=(cursor+1)%lenDirection
        newSpot=sumTuple(current, direction[cursor])            
        grid[newSpot]="#"
        current=newSpot
    end=current 
       
    border=set()
    border.add(start)
    newBorder=set()
    alreadyBeen=set()
    iteration=0
    while(True):
        for element in border:
            alreadyBeen.add(element)
            for d in direction:
                tentative=sumTuple(element,d)
                if(tentative==end):
                    return iteration+1
                if(tentative in grid or tentative in alreadyBeen):
                    continue
                newBorder.add(tentative)
        border=newBorder
        newBorder=set()
        iteration=iteration+1
        
def solve2():

    start=(0,0)
    orders=raw.split(',')
    cursor=0
    current=start
    
    
    arrOfPoints=[]
    arrOfPoints.append(start)
    for element in orders:
        if element[0]=="R":
            cursor=(cursor-1)%lenDirection
        else:
            cursor=(cursor+1)%lenDirection
        movement=mulTuple(direction[cursor], int(element[1:]))
        current=sumTuple(current, movement)
        arrOfPoints.append(current)
    end=current
    print(start)
    print("L",min([x[0] for x in arrOfPoints]))
    print("U",min([x[1] for x in arrOfPoints]))
    print("R", max([x[0] for x in arrOfPoints]))
    print("D",max([x[1] for x in arrOfPoints]))
    print(end)    

def solvePrint():
    start=(0,0)
    orders=raw.split(',')
    cursor=-1
    grid={}
    current=start
    
    
    for element in orders:
        if element[0]=="R":
            cursor=(cursor+1)%lenDirection
        else:
            cursor=(cursor-1)%lenDirection
        for _ in range((int(element[1:])*4)//1000000):
            newSpot=sumTuple(current, direction[cursor])            
            grid[newSpot]="#"
            current=newSpot
    end=current 
    grid[start]="S"
    grid[end]="E"
    minGridX=min([a[0] for a in grid.keys()])
    maxGridX=max([a[0] for a in grid.keys()])
    minGridY=min([a[1] for a in grid.keys()])
    maxGridY=max([a[1] for a in grid.keys()])
    
    for y in range(minGridY, maxGridY+1):
        for x in range(minGridX, maxGridX+1):
            if grid.get((x,y), None):
                print(grid[(x,y)], end="")
            else:
                print(" ", end="")
        print()
import heapq
def solveCompressed():
    start=(0,0)
    orders=raw.split(',')
    cursor=-1
    grid={}
    current=start

    arrOfPoints=[]
    arrOfPoints.append(start)
    arrOfPoints.append(sumTuple(current, direction[0]))
    arrOfPoints.append(sumTuple(current, direction[1]))
    arrOfPoints.append(sumTuple(current, direction[2]))
    arrOfPoints.append(sumTuple(current, direction[3]))
    for element in orders:
        if element[0]=="R":
            cursor=(cursor+1)%lenDirection
        else:
            cursor=(cursor-1)%lenDirection
        movement=mulTuple(direction[cursor], int(element[1:]))
        current=sumTuple(current, movement)
        arrOfPoints.append(current)
        arrOfPoints.append(sumTuple(current, direction[cursor]))
        arrOfPoints.append(sumTuple(current, direction[cursor-2]))
    arrOfPoints.append(sumTuple(current, direction[cursor-1]))
    arrOfPoints.append(sumTuple(current, direction[cursor-3]))

    arrPointX= list({x[0] for x in arrOfPoints})
    arrPointY=list({x[1] for x in arrOfPoints})
    
    arrPointX.sort()
    arrPointY.sort()
    xMap={x:i for i,x in enumerate(arrPointX)}
    yMap={y:i for i,y in enumerate(arrPointY)}
    orders=raw.split(",")
    cursor=-1
    grid={}
    numCurrent=(0,0)
    for element in orders:
        if element[0]=="R":
            cursor=(cursor+1)%lenDirection
        else:
            cursor=(cursor-1)%lenDirection
        
        newCurrent=sumTuple(numCurrent, mulTuple(direction[cursor],int(element[1:])))
        
        if cursor%2==1:
            minEl=min(yMap[newCurrent[1]], yMap[numCurrent[1]])
            maxEl=max(yMap[newCurrent[1]], yMap[numCurrent[1]])
          
            for a in range(minEl, maxEl+1):
                grid[(xMap[numCurrent[0]], a)]="#"
        else:
            minEl=min(xMap[newCurrent[0]], xMap[numCurrent[0]])
            maxEl=max(xMap[newCurrent[0]], xMap[numCurrent[0]])
            for a in range(minEl, maxEl+1):
                grid[(a, yMap[newCurrent[1]])]="#"
                
        numCurrent=newCurrent
    
    minGridX=min([a[0] for a in grid.keys()])
    maxGridX=max([a[0] for a in grid.keys()])
    minGridY=min([a[1] for a in grid.keys()])
    maxGridY=max([a[1] for a in grid.keys()])
    
    start=(xMap[0], yMap[0])
    end=(xMap[numCurrent[0]], yMap[numCurrent[1]])
    grid[end]="E"
    grid[start]="S"
    print(start, end)
    
            
    for y in range(minGridY, maxGridY+1):
        for x in range(minGridX, maxGridX+1):
            if grid.get((x,y), None):
                print(grid[(x,y)], end="")
            else:
                print(" ", end="")
        print()
    
    xThing={i:x for x,i in xMap.items()}
    yThing={i:y for y,i in yMap.items()}
    

    border=[]
    heapq.heappush(border, (0, (start[0], start[1])))
    alreadyBeen=set()
    while(border):
        score, current=heapq.heappop(border)
        
        if(current==end):
            return score
        if current in alreadyBeen:
            continue
        alreadyBeen.add(current)
        for i,d in enumerate(direction):
            
            tentative=sumTuple(current, d);
            
            if(tentative[0]<0 or tentative[0]>=len(xThing) or tentative[1]<0 or tentative[1]>=len(yThing)):
                continue
            if i%2==0:
                thingToUse=xThing
                idxToUse=0
            else:
                thingToUse=yThing
                idxToUse=1
            if grid.get(tentative, None)=="#":
                continue
            if tentative in alreadyBeen:
                continue
            newScore=score+(abs(thingToUse[current[idxToUse]]-thingToUse[tentative[idxToUse]]))
            heapq.heappush(border, (newScore, tentative))
            
        
print("result:", solveCompressed())
