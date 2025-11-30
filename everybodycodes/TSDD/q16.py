raw=""""""

import math


def solve():
    elements=[int(x) for x in raw.split(",")]
    end=90
    sumz=0
    for element in elements:
        sumz=sumz+end//element
    return sumz

def addElementToExpected(expected, element):
    current=element
    while current<len(expected):
        expected[current]=expected[current]+1
        current=current+element

def solve2():
    elements=[int(x) for x in raw.split(",")]
    expected=[0]*len(elements)
    expected.append(0)
    current=1
    elements.insert(0, 0)
    results=[]
    while(current<len(elements)):
        if elements[current]!=expected[current]:
            addElementToExpected(expected, current)
            results.append(current)
        current=current+1
        
    mult=1
    for element in results:
        mult=mult*element
        
    return mult

def lcm(a,b):
    return a*b//math.gcd(a,b)

def solve3():
    blocks=202520252025000
    elements=[int(x) for x in raw.split(",")]
    expected=[0]*len(elements)
    expected.append(0)
    current=1
    elements.insert(0, 0)
    results=[]
    while(current<len(elements)):
        if elements[current]!=expected[current]:
            addElementToExpected(expected, current)
            results.append(current)
        current=current+1
    
    elements=results
    end=2
    oldEnd=0
    while(True):
        #print(end)
        sumz=0
        for element in elements:
            sumz=sumz+end//element
        if sumz<blocks:
            oldEnd=end
            end=end*2
        else:
            if(end-oldEnd)==1:
                return oldEnd
            end=(oldEnd+end)//2    
    
    
""" #old approach, not good if bad lcm (which it is) i try dicotomy search instead 
    theLcm=results[0]
    for element in results:
        theLcm=lcm(theLcm, element)
    print(results, theLcm)
    columnsRepeating=theLcm
    end=columnsRepeating
    start=1
    sumz=0
    for element in results:
        sumz=sumz+end//element
    print("for col:", end)
    print("we need blocks:", sumz)
    filledColumns=(blocks//sumz)*columnsRepeating
    remaining=blocks%sumz
    print("we manage to fill a grand totals of: ", filledColumns)
    print("but there are remaining blocks: ", remaining)
    cursor=1
    while(True):
        for element in results:
            if cursor%element==0:
                remaining=remaining-1    
        if remaining<0:
            break
        else:
            filledColumns=filledColumns+1
    return filledColumns
"""

print("result: ", solve3())
