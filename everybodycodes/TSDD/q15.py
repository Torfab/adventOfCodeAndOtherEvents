import heapq

raw="""R8699217,R2897941,R9693113,R599574,L9093539,R5697777,R9799118,R2699757,L199846,L5296237,R1799838,L7597796,R3199072,R4198362,L4998050,R2198306,L2899739,R9493255,R2399304,L1299883,R6397504,L1599376,R6999370,L9197332,R7297883,R4398724,L9696217,R3197728,R4696381,L9898911,R299967,R8593894,L4596458,L2997690,L399716,R6698057,R8793224,L7097941,L8093763,R7099219,R9598944,R1399006,L2897941,L7996880,R2498075,R799384,L5999460,R1099153,L8897419,R7097231,R5196308,L7599164,L4296947,R599766,R2199142,L2099391,L7299197,R6399296,R8093763,L6699397,R9298977,L4199538,R6794764,R3299703,L2499275,L4398284,L3197536,R999230,L7694071,R5899351,R7499175,R3599604,L3097799,L2897767,R5699373,L8493455,R1399006,R899901,L8294107,R2899159,R9297303,L3697373,L3199712,R6397504,L1898537,R1598768,L4698167,R1699847,L1499415,L5099541,R2999670,R4599494,L2799692,R2598154,R3797302,L8297593,R1798614,L7199352,R5699487,L4298323,L5998260,R9293397,R7599316,R2399304,R4099631,L2799748,R2899681,L2499725,L7694071,L7896919,R5297933,L9597216,R6298173,R6298173,L2499275,L599934,R2099811,L9193468,R7894391,R899919,R1399454,L6395072,L9197332,R6099451,L199982,R9193468,L999610,L6698057,R8897419,R7799298,R9597216,L3498985,L7299343,R3097799,L4998050,R3998440,R5699373,L6899241,R2599246,L8397564,R4998050,L7996880,R1399874,R3099659,L6899379,L3099659,R5098011,L7094533,R8499235,R7199208,R6599274,L1099571,L2099181,R399956,L4799568,L6794764,R4296947,R399844,L4099631,R1499565,L5899351,L4299527,R5999340,R6397504,R4199622,L2398296,R2199758,L499855,L6098231,R999710,L2599246,R399884,L7394746,R8493455,L9099181,R5799478,R2198438,R2798012,L3299637,L6994610,R9692531,R5695611,L499805,L6197582,L7799142,R699503,R7794462,L5697777,L9698933,R3499615,R4699577,L6099451,R5599496,R1599856,R5396166,L6099451,L5298463,R6494995,L1598768,L7494225,L6099451,R899919,R5099541,L4396612,R2999670,L1898651,R1498935,L3097799,L1399454,R1399846,L8396724,R6699397,R3799582,L9593184,R1798614,R1499865,R799384,L3797302,L1299857,R6894687,R4896227,L799928,L5699487,R599574,L7397854,L3399014,R3896997,L6297543,R199858,R3498635,L4299527,L8499235,R1999820,R4198362,L7497075,L1099153,R1499865,L1699813,R2999670,L4699483"""

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
        newSpot=sumtuple(current, direction[cursor])            
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
    grid={}
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
        for a in range((int(element[1:])*4)//1000000):
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
    end=current

    arrPointX=list(set([x[0] for x in arrOfPoints]))
    arrPointY=list(set([x[1] for x in arrOfPoints]))
    
    arrPointX.sort()
    arrPointY.sort()
    xMap={x:i for i,x in enumerate(arrPointX)}
    yMap={y:i for i,y in enumerate(arrPointY)}
    
    start=(xMap[0], yMap[0])
    orders=raw.split(",")
    cursor=-1
    grid={}
    current=start
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
