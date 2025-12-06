
def parseRows(raw):
    state=0
    ranges=[]
    items=[]
    for row in raw:
       if state==0:
            if row=="":
                state=1
                continue
            rowSplitted=row.split("-") 
            ranges.append((int(rowSplitted[0]), int(rowSplitted[1])))
       elif state==1:
           items.append(int(row))
    return ranges, items
    
def isInRanges(item, ranges):
    for portion in ranges:
        if(item>=portion[0] and item<=[1]):
            return True
    return False
    
def solve():
    ranges, items=parseRows(raw)    
    count=0
    for item in items:
        if isInRanges(item, ranges):
            count=count+1
    
    return count

def insertElementInResult(portion, results):
    inserted=False
    for idx in range(len(results)):
        element=results[idx]
        if portion==element:
            return None
        if portion[1]<element[0] or portion[0]>element[1]:
            continue
        if portion[0]>=element[0] and portion[1]<=element[1]:
            return None
        if portion[0]<=element[0] and portion[1]>=element[1]:
            results.pop(idx)
            return portion
        if portion[0]<=element[1] and portion[1]>=element[1]:
            results.pop(idx)
            return (min(portion[0], element[0]), max(portion[1], element[1]))
        if portion[1]>=element[0] and portion[0]<=element[0]:
            results.pop(idx)
            return (min(portion[0], element[0]), max(portion[1], element[1]))
    results.append(portion) 
    return None
            
        

def solve2():
    ranges, _=parseRows(raw)
    results=[]

    count=0    
    for portion in ranges:
        while(portion):
            portion=insertElementInResult(portion, results)
    
    for element in results:
        count=count+element[1]-element[0]+1    
    return count
print(solve2())

